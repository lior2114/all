// Content script: finds <video> elements and injects Download + Record (non-DRM) buttons

(function initVideoButtons() {
  // Add styles once
  const styleId = 'qvd-style';
  if (!document.getElementById(styleId)) {
    const style = document.createElement('style');
    style.id = styleId;
    style.textContent = `
      .qvd-btns { position: absolute; top: 8px; right: 8px; z-index: 999999; display: flex; gap: 8px; }
      .qvd-download-btn { position: static; background: rgba(0,0,0,0.7); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-record-btn { position: static; background: rgba(0,128,0,0.75); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-pause-btn { position: static; background: rgba(128,128,0,0.85); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-copy-btn { position: static; background: rgba(0,0,0,0.55); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-cc-btn { position: static; background: rgba(0,0,0,0.55); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-speed-btn { position: static; background: rgba(0,100,200,0.8); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-segment-btn { position: static; background: rgba(200,100,0,0.8); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-extract-btn { position: static; background: rgba(150,0,150,0.8); color: #fff; border: none; padding: 6px 10px; border-radius: 4px; cursor: pointer; font-size: 12px; }
      .qvd-recording { background: rgba(200,0,0,0.85) !important; }
      .qvd-video-wrapper {
        position: relative !important;
        display: inline-block;
      }
    `;
    document.documentElement.appendChild(style);
  }

  const siteOrigin = location.origin;
  let siteEnabled = true; // default enabled unless explicitly disabled
  let options = { delayStart3s: false };

  async function loadSettings() {
    try {
      const data = await chrome.storage.sync.get({ sites: {}, options: {} });
      const sites = data.sites || {};
      siteEnabled = sites[siteOrigin] !== false;
      options = Object.assign({ delayStart3s: false }, data.options || {});
    } catch (_) {}
  }

  function unwrapAllUI() {
    const wrappers = Array.from(document.querySelectorAll('.qvd-video-wrapper'));
    for (const wrapper of wrappers) {
      const video = wrapper.querySelector('video');
      if (video && wrapper.parentElement) {
        video.dataset.qvdProcessed = '';
        wrapper.parentElement.insertBefore(video, wrapper);
        wrapper.remove();
      }
    }
  }

  const recordState = new WeakMap();

  function getBestVideoSource(video) {
    // Prefer 'src' attribute; fallback to first <source> with src
    if (video.src) return video.src;
    const sources = Array.from(video.querySelectorAll('source'));
    const withSrc = sources.map(s => s.src).filter(Boolean);
    return withSrc.length ? withSrc[0] : null;
  }

  function canRecordVideo(video) {
    // captureStream is typically blocked for DRM-protected content
    return typeof video.captureStream === 'function' && typeof MediaRecorder !== 'undefined';
  }

  function addButtonsToVideo(video) {
    if (video.dataset.qvdProcessed === '1') return;
    video.dataset.qvdProcessed = '1';

    const sourceUrl = getBestVideoSource(video);
    const downloadable = !!sourceUrl && !(sourceUrl.startsWith('blob:') || sourceUrl.startsWith('data:'));

    // Wrap video if necessary to position the button
    const wrapper = document.createElement('div');
    wrapper.className = 'qvd-video-wrapper';
    const parent = video.parentElement;
    if (!parent) return;
    parent.insertBefore(wrapper, video);
    wrapper.appendChild(video);

    const btnRow = document.createElement('div');
    btnRow.className = 'qvd-btns';
    wrapper.appendChild(btnRow);

    if (downloadable) {
      const dlBtn = document.createElement('button');
      dlBtn.className = 'qvd-download-btn';
      dlBtn.textContent = 'Download';
      dlBtn.title = 'Download this video source';
      dlBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const url = getBestVideoSource(video);
        if (!url) return;

        const filename = (video.getAttribute('data-title') || document.title || 'video')
          .replace(/[^\w\u0590-\u05FF\-\.\s]/g, '_') + '.mp4';

        chrome.runtime.sendMessage(
          { type: 'DOWNLOAD_VIDEO', url, filename },
          (resp) => {
            if (!resp || !resp.ok) {
              console.warn('Download failed', resp && resp.error);
            }
          }
        );
      });
      btnRow.appendChild(dlBtn);
    }

    // Copy URL (works for direct URLs; blob: URLs are only valid in this tab)
    if (sourceUrl) {
      const copyBtn = document.createElement('button');
      copyBtn.className = 'qvd-copy-btn';
      copyBtn.textContent = 'Copy URL';
      copyBtn.title = 'Copy video URL to clipboard';
      copyBtn.addEventListener('click', async (e) => {
        e.stopPropagation();
        const url = getBestVideoSource(video);
        if (!url) return;
        try {
          await navigator.clipboard.writeText(url);
        } catch (err) {
          console.warn('Clipboard failed', err);
        }
      });
      btnRow.appendChild(copyBtn);
    }

    // Subtitles download (first available track)
    (function addSubtitleButton() {
      const tracks = Array.from(video.querySelectorAll('track'))
        .filter(t => (t.kind === 'subtitles' || t.kind === 'captions') && t.src);
      if (!tracks.length) return;
      const ccBtn = document.createElement('button');
      ccBtn.className = 'qvd-cc-btn';
      ccBtn.textContent = 'CC';
      ccBtn.title = 'Download subtitles/captions';
      ccBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const t = tracks[0];
        const url = t.src;
        if (!url) return;
        const label = (t.label || t.srclang || 'subtitles')
          .replace(/[^\w\u0590-\u05FF\-\.\s]/g, '_');
        let ext = '.vtt';
        try {
          const u = new URL(url);
          const m = u.pathname.match(/\.([a-zA-Z0-9]+)$/);
          if (m) ext = '.' + m[1];
        } catch (_) {}
        const base = (video.getAttribute('data-title') || document.title || 'subs')
          .replace(/[^\w\u0590-\u05FF\-\.\s]/g, '_');
        const filename = base + '.' + label + ext;
        chrome.runtime.sendMessage(
          { type: 'DOWNLOAD_VIDEO', url, filename },
          (resp) => {
            if (!resp || !resp.ok) console.warn('Subtitle download failed', resp && resp.error);
          }
        );
      });
      btnRow.appendChild(ccBtn);
    })();

    if (canRecordVideo(video)) {
      const recBtn = document.createElement('button');
      recBtn.className = 'qvd-record-btn';
      recBtn.textContent = 'Record';
      recBtn.title = 'Record this video (non-DRM) to a file';

      const pauseBtn = document.createElement('button');
      pauseBtn.className = 'qvd-pause-btn';
      pauseBtn.textContent = 'Pause';
      pauseBtn.title = 'Pause/Resume recording';
      pauseBtn.disabled = true;

      function pickMimeType() {
        const candidates = [
          'video/webm;codecs=vp9,opus',
          'video/webm;codecs=vp8,opus',
          'video/webm'
        ];
        for (const c of candidates) {
          if (typeof MediaRecorder.isTypeSupported === 'function' && MediaRecorder.isTypeSupported(c)) {
            return c;
          }
        }
        return '';
      }

      function startRecording() {
        try {
          const stream = video.captureStream();
          const mimeType = pickMimeType();
          const recorder = new MediaRecorder(stream, mimeType ? { mimeType } : undefined);
          const chunks = [];

          recorder.ondataavailable = (ev) => {
            if (ev.data && ev.data.size > 0) chunks.push(ev.data);
          };
          recorder.onstop = () => {
            try {
              const type = recorder.mimeType || mimeType || 'video/webm';
              const blob = new Blob(chunks, { type });
              const url = URL.createObjectURL(blob);
              const filenameBase = (video.getAttribute('data-title') || document.title || 'video')
                .replace(/[^\w\u0590-\u05FF\-\.\s]/g, '_');
              const filename = filenameBase + (type.includes('webm') ? '.webm' : '.webm');
              const a = document.createElement('a');
              a.href = url;
              a.download = filename;
              document.body.appendChild(a);
              a.click();
              a.remove();
              setTimeout(() => URL.revokeObjectURL(url), 10_000);
            } finally {
              recBtn.textContent = 'Record';
              recBtn.classList.remove('qvd-recording');
              pauseBtn.disabled = true;
              pauseBtn.textContent = 'Pause';
              recordState.delete(video);
            }
          };

          // Stop when video ends
          const onEnded = () => {
            try { recorder.state !== 'inactive' && recorder.stop(); } catch (_) {}
            video.removeEventListener('ended', onEnded);
          };
          video.addEventListener('ended', onEnded);

          recordState.set(video, { recorder, onEnded });

          const startNow = () => {
            try { recorder.start(1000); } catch (e) { console.warn('recorder start failed', e); }
            recBtn.textContent = 'Stop';
            recBtn.classList.add('qvd-recording');
            pauseBtn.disabled = false;
            // Ensure playback for capture
            if (video.paused) {
              video.play().catch(() => {});
            }
          };

          if (options && options.delayStart3s) {
            recBtn.textContent = 'Starting…';
            setTimeout(startNow, 3000);
          } else {
            startNow();
          }
        } catch (err) {
          console.warn('Recording failed to start', err);
        }
      }

      function stopRecording() {
        const state = recordState.get(video);
        if (!state) return;
        try {
          if (state.recorder && state.recorder.state !== 'inactive') {
            state.recorder.stop();
          }
        } catch (err) {
          console.warn('Error stopping recorder', err);
        } finally {
          if (state.onEnded) {
            video.removeEventListener('ended', state.onEnded);
          }
        }
      }

      recBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const state = recordState.get(video);
        if (!state) {
          startRecording();
        } else {
          stopRecording();
        }
      });

      pauseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        const state = recordState.get(video);
        if (!state || !state.recorder) return;
        try {
          if (state.recorder.state === 'recording') {
            state.recorder.pause();
            pauseBtn.textContent = 'Resume';
          } else if (state.recorder.state === 'paused') {
            state.recorder.resume();
            pauseBtn.textContent = 'Pause';
          }
        } catch (err) {
          console.warn('Pause/resume failed', err);
        }
      });

      btnRow.appendChild(recBtn);
      btnRow.appendChild(pauseBtn);
    }

    // Speed control button
    const speedBtn = document.createElement('button');
    speedBtn.className = 'qvd-speed-btn';
    speedBtn.textContent = 'Speed';
    speedBtn.title = 'Change playback speed (1x-15x)';
    
    let currentSpeed = 1;
    const speeds = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.5, 3, 4, 5, 6, 8, 10, 12, 15];
    let speedIndex = speeds.indexOf(1);
    
    speedBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      speedIndex = (speedIndex + 1) % speeds.length;
      currentSpeed = speeds[speedIndex];
      video.playbackRate = currentSpeed;
      speedBtn.textContent = currentSpeed + 'x';
    });
    
    btnRow.appendChild(speedBtn);

    // Segment recording button
    const segmentBtn = document.createElement('button');
    segmentBtn.className = 'qvd-segment-btn';
    segmentBtn.textContent = 'Segment';
    segmentBtn.title = 'Record only a segment (set start/end times)';
    
    let segmentStart = null;
    let segmentEnd = null;
    let isSegmentMode = false;
    
    segmentBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      
      if (!isSegmentMode) {
        // Set start time
        segmentStart = video.currentTime;
        segmentBtn.textContent = 'Set End';
        segmentBtn.title = 'Click to set end time for segment recording';
        isSegmentMode = true;
        alert(`Start time set to ${Math.floor(segmentStart / 60)}:${Math.floor(segmentStart % 60).toString().padStart(2, '0')}`);
      } else {
        // Set end time and start recording
        segmentEnd = video.currentTime;
        if (segmentEnd <= segmentStart) {
          alert('End time must be after start time!');
          return;
        }
        
        const duration = segmentEnd - segmentStart;
        alert(`Segment set: ${Math.floor(segmentStart / 60)}:${Math.floor(segmentStart % 60).toString().padStart(2, '0')} to ${Math.floor(segmentEnd / 60)}:${Math.floor(segmentEnd % 60).toString().padStart(2, '0')} (${Math.floor(duration / 60)}:${Math.floor(duration % 60).toString().padStart(2, '0')})`);
        
        // Start segment recording
        startSegmentRecording();
        
        // Reset button
        segmentBtn.textContent = 'Segment';
        segmentBtn.title = 'Record only a segment (set start/end times)';
        isSegmentMode = false;
        segmentStart = null;
        segmentEnd = null;
      }
    });
    
    function startSegmentRecording() {
      if (!canRecordVideo(video)) {
        alert('Segment recording not supported for this video');
        return;
      }
      
      try {
        const stream = video.captureStream();
        const mimeType = pickMimeType();
        const recorder = new MediaRecorder(stream, mimeType ? { mimeType } : undefined);
        const chunks = [];
        
        // Jump to start time
        video.currentTime = segmentStart;
        
        recorder.ondataavailable = (ev) => {
          if (ev.data && ev.data.size > 0) chunks.push(ev.data);
        };
        
        recorder.onstop = () => {
          try {
            const type = recorder.mimeType || mimeType || 'video/webm';
            const blob = new Blob(chunks, { type });
            const url = URL.createObjectURL(blob);
            const filenameBase = (video.getAttribute('data-title') || document.title || 'video')
              .replace(/[^\w\u0590-\u05FF\-\.\s]/g, '_');
            const filename = filenameBase + '_segment_' + Math.floor(segmentStart) + 's_to_' + Math.floor(segmentEnd) + 's' + (type.includes('webm') ? '.webm' : '.webm');
            const a = document.createElement('a');
            a.href = url;
            a.download = filename;
            document.body.appendChild(a);
            a.click();
            a.remove();
            setTimeout(() => URL.revokeObjectURL(url), 10_000);
          } catch (err) {
            console.warn('Error saving segment recording', err);
          }
        };
        
        // Start recording
        recorder.start(1000);
        
        // Play video at segment start
        video.play().catch(() => {});
        
        // Stop recording when we reach end time
        const checkTime = () => {
          if (video.currentTime >= segmentEnd) {
            recorder.stop();
            video.pause();
          } else {
            requestAnimationFrame(checkTime);
          }
        };
        checkTime();
        
        alert('Segment recording started!');
        
      } catch (err) {
        console.warn('Segment recording failed', err);
        alert('Segment recording failed: ' + err.message);
      }
    }
    
    btnRow.appendChild(segmentBtn);

    // Extract segment button (direct extraction without recording)
    const extractBtn = document.createElement('button');
    extractBtn.className = 'qvd-extract-btn';
    extractBtn.textContent = 'Extract';
    extractBtn.title = 'Extract video segment directly (set start/end times)';
    
    let extractStart = null;
    let extractEnd = null;
    let isExtractMode = false;
    
    extractBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      
      if (!isExtractMode) {
        // Set start time
        extractStart = video.currentTime;
        extractBtn.textContent = 'Set End';
        extractBtn.title = 'Click to set end time for segment extraction';
        isExtractMode = true;
        alert(`Start time set to ${Math.floor(extractStart / 60)}:${Math.floor(extractStart % 60).toString().padStart(2, '0')}`);
      } else {
        // Set end time and extract segment
        extractEnd = video.currentTime;
        if (extractEnd <= extractStart) {
          alert('End time must be after start time!');
          return;
        }
        
        const duration = extractEnd - extractStart;
        alert(`Extracting segment: ${Math.floor(extractStart / 60)}:${Math.floor(extractStart % 60).toString().padStart(2, '0')} to ${Math.floor(extractEnd / 60)}:${Math.floor(extractEnd % 60).toString().padStart(2, '0')} (${Math.floor(duration / 60)}:${Math.floor(duration % 60).toString().padStart(2, '0')})`);
        
        // Extract segment
        extractSegment();
        
        // Reset button
        extractBtn.textContent = 'Extract';
        extractBtn.title = 'Extract video segment directly (set start/end times)';
        isExtractMode = false;
        extractStart = null;
        extractEnd = null;
      }
    });
    
    function extractSegment() {
      // Try multiple extraction methods
      const sourceUrl = getBestVideoSource(video);
      
      if (sourceUrl && !sourceUrl.startsWith('blob:') && !sourceUrl.startsWith('data:')) {
        // Method 1: Direct source extraction
        extractFromSource(sourceUrl);
      } else {
        // Method 2: Canvas-based extraction from current video
        extractFromCanvas();
      }
    }
    
    function extractFromSource(sourceUrl) {
      const extractVideo = document.createElement('video');
      extractVideo.crossOrigin = 'anonymous';
      extractVideo.muted = true;
      extractVideo.preload = 'metadata';
      
      extractVideo.addEventListener('loadedmetadata', () => {
        try {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          
          // Set proper canvas dimensions
          const videoWidth = extractVideo.videoWidth || 640;
          const videoHeight = extractVideo.videoHeight || 480;
          
          canvas.width = videoWidth;
          canvas.height = videoHeight;
          canvas.style.width = videoWidth + 'px';
          canvas.style.height = videoHeight + 'px';
          
          const stream = canvas.captureStream(30);
          const mimeType = pickMimeType();
          
          // Use better recording options
          const recorderOptions = {
            mimeType: mimeType,
            videoBitsPerSecond: 2500000, // 2.5 Mbps for good quality
            audioBitsPerSecond: 128000   // 128 kbps for audio
          };
          
          const recorder = new MediaRecorder(stream, recorderOptions);
          const chunks = [];
          
          recorder.ondataavailable = (ev) => {
            if (ev.data && ev.data.size > 0) chunks.push(ev.data);
          };
          
          recorder.onstop = () => {
            saveExtractedVideo(chunks, mimeType);
          };
          
          recorder.start(200); // Record every 200ms for better quality
          
          extractVideo.currentTime = extractStart;
          
          // Wait for video to be ready
          const waitForVideo = () => {
            if (extractVideo.readyState >= 2) { // HAVE_CURRENT_DATA
              startSourceExtraction();
            } else {
              setTimeout(waitForVideo, 100);
            }
          };
          
          const startSourceExtraction = () => {
            extractVideo.play().then(() => {
              let frameCount = 0;
              const targetFPS = 30;
              const frameInterval = 1000 / targetFPS;
              let lastFrameTime = 0;
              
              const drawFrame = (currentTime) => {
                if (extractVideo.currentTime >= extractEnd || extractVideo.paused || extractVideo.ended) {
                  recorder.stop();
                  extractVideo.pause();
                  return;
                }
                
                // Only draw frame at target FPS
                if (currentTime - lastFrameTime >= frameInterval) {
                  try {
                    // Clear canvas first
                    ctx.clearRect(0, 0, canvas.width, canvas.height);
                    
                    // Draw current frame to canvas
                    ctx.drawImage(extractVideo, 0, 0, canvas.width, canvas.height);
                    
                    frameCount++;
                    lastFrameTime = currentTime;
                  } catch (drawErr) {
                    console.warn('Error drawing frame:', drawErr);
                  }
                }
                
                requestAnimationFrame(drawFrame);
              };
              
              requestAnimationFrame(drawFrame);
            }).catch(err => {
              console.warn('Error playing video for extraction, trying canvas method', err);
              extractFromCanvas();
            });
          };
          
          waitForVideo();
          
        } catch (err) {
          console.warn('Error setting up source extraction, trying canvas method', err);
          extractFromCanvas();
        }
      });
      
      extractVideo.addEventListener('error', (err) => {
        console.warn('Error loading video source, trying canvas method', err);
        extractFromCanvas();
      });
      
      extractVideo.src = sourceUrl;
    }
    
    function extractFromCanvas() {
      try {
        // Use the current video element directly
        const canvas = document.createElement('canvas');
        const ctx = canvas.getContext('2d');
        
        // Set canvas size to match current video with proper dimensions
        const videoWidth = video.videoWidth || video.offsetWidth || 640;
        const videoHeight = video.videoHeight || video.offsetHeight || 480;
        
        canvas.width = videoWidth;
        canvas.height = videoHeight;
        
        // Ensure canvas is properly sized
        canvas.style.width = videoWidth + 'px';
        canvas.style.height = videoHeight + 'px';
        
        const stream = canvas.captureStream(30);
        const mimeType = pickMimeType();
        
        // Use better recording options
        const recorderOptions = {
          mimeType: mimeType,
          videoBitsPerSecond: 2500000, // 2.5 Mbps for good quality
          audioBitsPerSecond: 128000   // 128 kbps for audio
        };
        
        const recorder = new MediaRecorder(stream, recorderOptions);
        const chunks = [];
        
        recorder.ondataavailable = (ev) => {
          if (ev.data && ev.data.size > 0) {
            chunks.push(ev.data);
          }
        };
        
        recorder.onstop = () => {
          saveExtractedVideo(chunks, mimeType);
        };
        
        // Start recording with higher frequency for better quality
        recorder.start(200); // Record every 200ms
        
        // Store original playback rate and time
        const originalRate = video.playbackRate;
        const originalTime = video.currentTime;
        const originalPaused = video.paused;
        
        // Set to start time and play
        video.currentTime = extractStart;
        video.playbackRate = 1; // Ensure normal speed for extraction
        
        // Wait for video to be ready
        const waitForVideo = () => {
          if (video.readyState >= 2) { // HAVE_CURRENT_DATA
            startExtraction();
          } else {
            setTimeout(waitForVideo, 100);
          }
        };
        
        const startExtraction = () => {
          video.play().then(() => {
            let frameCount = 0;
            const targetFPS = 30;
            const frameInterval = 1000 / targetFPS;
            let lastFrameTime = 0;
            
            const drawFrame = (currentTime) => {
              if (video.currentTime >= extractEnd || video.paused || video.ended) {
                recorder.stop();
                video.pause();
                // Restore original settings
                video.playbackRate = originalRate;
                video.currentTime = originalTime;
                if (originalPaused) {
                  video.pause();
                }
                return;
              }
              
              // Only draw frame at target FPS
              if (currentTime - lastFrameTime >= frameInterval) {
                try {
                  // Clear canvas first
                  ctx.clearRect(0, 0, canvas.width, canvas.height);
                  
                  // Draw current frame to canvas with proper scaling
                  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                  
                  frameCount++;
                  lastFrameTime = currentTime;
                } catch (drawErr) {
                  console.warn('Error drawing frame:', drawErr);
                }
              }
              
              requestAnimationFrame(drawFrame);
            };
            
            requestAnimationFrame(drawFrame);
          }).catch(err => {
            console.warn('Error playing video for canvas extraction', err);
            recorder.stop();
            video.playbackRate = originalRate;
            video.currentTime = originalTime;
            if (originalPaused) {
              video.pause();
            }
            alert('Error extracting segment: ' + err.message);
          });
        };
        
        waitForVideo();
        
      } catch (err) {
        console.warn('Error setting up canvas extraction', err);
        alert('Error setting up extraction: ' + err.message);
      }
    }
    
    function saveExtractedVideo(chunks, mimeType) {
      try {
        const type = mimeType || 'video/webm';
        const blob = new Blob(chunks, { type });
        const url = URL.createObjectURL(blob);
        const filenameBase = (video.getAttribute('data-title') || document.title || 'video')
          .replace(/[^\w\u0590-\u05FF\-\.\s]/g, '_');
        const filename = filenameBase + '_extracted_' + Math.floor(extractStart) + 's_to_' + Math.floor(extractEnd) + 's' + (type.includes('webm') ? '.webm' : '.webm');
        const a = document.createElement('a');
        a.href = url;
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(() => URL.revokeObjectURL(url), 10_000);
        
        alert('Segment extracted successfully!');
      } catch (err) {
        console.warn('Error saving extracted segment', err);
        alert('Error saving extracted segment: ' + err.message);
      }
    }
    
    btnRow.appendChild(extractBtn);
  }

  function scan() {
    if (!siteEnabled) return;
    const videos = Array.from(document.querySelectorAll('video'));
    videos.forEach(addButtonsToVideo);
  }

  // Initial scan and observe for dynamically added videos
  (async function bootstrap() {
    await loadSettings();
    if (siteEnabled) scan();
  })();

  const mo = new MutationObserver(() => scan());
  mo.observe(document.documentElement, { childList: true, subtree: true, attributes: false });

  chrome.runtime.onMessage.addListener((message) => {
    if (!message || typeof message.type !== 'string') return;
    if (message.type === 'QVD_SITE_ENABLE_CHANGED' || message.type === 'QVD_OPTIONS_CHANGED') {
      loadSettings().then(() => {
        if (siteEnabled) {
          scan();
        } else {
          unwrapAllUI();
        }
      });
    }
  });
})();


