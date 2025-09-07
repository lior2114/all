// Background service worker for handling downloads

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message && message.type === 'DOWNLOAD_VIDEO' && typeof message.url === 'string') {
    const suggestedFilename = message.filename || 'video.mp4';
    chrome.downloads.download(
      {
        url: message.url,
        filename: suggestedFilename,
        saveAs: true
      },
      (downloadId) => {
        if (chrome.runtime.lastError) {
          sendResponse({ ok: false, error: chrome.runtime.lastError.message });
          return;
        }
        sendResponse({ ok: true, downloadId });
      }
    );
    // Indicate we'll respond asynchronously
    return true;
  }
});


