import React, { useEffect, useRef, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { lessons } from '../data/lessons';
import Keyboard from './Keyboard';
import './LessonContent.css';

const TranslatedHebrewLesson = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [currentLesson, setCurrentLesson] = useState(null);
  const [activeText, setActiveText] = useState('');
  const [currentCharIndex, setCurrentCharIndex] = useState(0);
  const [inputValue, setInputValue] = useState('');
  const [isActive, setIsActive] = useState(false);
  const [isCompleted, setIsCompleted] = useState(false);
  const [startTime, setStartTime] = useState(null);
  const [endTime, setEndTime] = useState(null);
  const [typingData, setTypingData] = useState({
    errors: 0,
    errorsByChar: new Map(),
    startTime: null,
    endTime: null,
  });
  const [hasErrorOnCurrentChar, setHasErrorOnCurrentChar] = useState(false);
  const inputRef = useRef(null);

  useEffect(() => {
    const lessonId = parseInt(id);
    const lesson = (lessons.hebrew || []).find((l) => l.id === lessonId);
    if (!lesson) {
      navigate('/translated-hebrew-lessons');
      return;
    }
    setCurrentLesson(lesson);

    const shuffleTokens = (text) => {
      if (!text) return '';
      const tokens = text.split(' ');
      for (let i = tokens.length - 1; i > 0; i -= 1) {
        const j = Math.floor(Math.random() * (i + 1));
        [tokens[i], tokens[j]] = [tokens[j], tokens[i]];
      }
      return tokens.join(' ');
    };

    setActiveText(shuffleTokens(lesson.text));
    setCurrentCharIndex(0);
    setInputValue('');
    setIsActive(false);
    setIsCompleted(false);
    setStartTime(null);
    setEndTime(null);
    setHasErrorOnCurrentChar(false);
    setTypingData({ errors: 0, errorsByChar: new Map(), startTime: null, endTime: null });
  }, [id, navigate]);

  useEffect(() => {
    if (currentLesson && inputRef.current && !isCompleted) {
      inputRef.current.focus();
    }
  }, [currentLesson, isCompleted]);

  const handleInputChange = (e) => {
    if (!isActive || isCompleted) return;

    const input = e.target.value;
    const currentChar = activeText[currentCharIndex];

    setInputValue(input);

    if (input === currentChar) {
      setCurrentCharIndex((prev) => prev + 1);
      setInputValue('');
      setHasErrorOnCurrentChar(false);

      if (currentCharIndex + 1 >= activeText.length) {
        setEndTime(Date.now());
        setTypingData((prev) => ({ ...prev, endTime: Date.now() }));
        setIsActive(false);
        setIsCompleted(true);
      }
    } else if (input.length > 0) {
      if (input.length === 1 && !hasErrorOnCurrentChar) {
        setTypingData((prev) => ({
          ...prev,
          errors: prev.errors + 1,
          errorsByChar: new Map(prev.errorsByChar).set(currentChar, (prev.errorsByChar.get(currentChar) || 0) + 1),
        }));
        setHasErrorOnCurrentChar(true);
      }
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Escape') {
      navigate('/translated-hebrew-lessons');
    }
  };

  const handleKeyUp = () => {
    setHasErrorOnCurrentChar(false);
  };

  const calculateProgress = () => {
    if (!currentLesson) return 0;
    return Math.round((currentCharIndex / (activeText.length || 1)) * 100);
  };

  const calculateCPM = () => {
    if (!startTime) return 0;
    const endTs = isCompleted && endTime ? endTime : (isActive ? Date.now() : null);
    if (!endTs) return 0;
    const elapsed = (endTs - startTime) / 1000 / 60;
    return elapsed > 0 ? Math.round(currentCharIndex / elapsed) : 0;
  };

  const calculateAccuracy = () => {
    const total = currentCharIndex + typingData.errors;
    return total > 0 ? Math.round((currentCharIndex / total) * 100) : 100;
  };

  const getCurrentKey = () => {
    if (!currentLesson || currentCharIndex >= activeText.length) return null;
    return activeText[currentCharIndex];
  };

  const getCurrentKeys = () => {
    if (!currentLesson) return [];
    return currentLesson.keys;
  };

  const restartLesson = () => {
    setCurrentCharIndex(0);
    setInputValue('');
    setIsActive(false);
    setIsCompleted(false);
    setStartTime(null);
    setEndTime(null);
    setHasErrorOnCurrentChar(false);
    setTypingData({ errors: 0, errorsByChar: new Map(), startTime: null, endTime: null });

    if (currentLesson?.text) {
      const tokens = currentLesson.text.split(' ');
      for (let i = tokens.length - 1; i > 0; i -= 1) {
        const j = Math.floor(Math.random() * (i + 1));
        [tokens[i], tokens[j]] = [tokens[j], tokens[i]];
      }
      setActiveText(tokens.join(' '));
    }

    if (inputRef.current) {
      inputRef.current.focus();
    }
  };

  if (!currentLesson) {
    return <div>Loading...</div>;
  }

  if (isCompleted) {
    const finalCPM = calculateCPM();
    const finalAccuracy = calculateAccuracy();
    const timeElapsed = endTime && startTime ? Math.round((endTime - startTime) / 1000) : 0;

    return (
      <div className="lesson-content" dir="ltr">
        <div className="lesson-container">
          <div className="lesson-results card">
            <h2>{finalAccuracy >= 80 ? 'You passed!' : 'Did not meet requirements'}</h2>

            <div className="results-stats">
              <div className="result-stat">
                <div className="stat-value">{finalCPM}</div>
                <div>CPM</div>
              </div>
              <div className="result-stat">
                <div className="stat-value">{finalAccuracy}%</div>
                <div>Accuracy</div>
              </div>
              <div className="result-stat">
                <div className="stat-value">{timeElapsed}s</div>
                <div>Time</div>
              </div>
              <div className="result-stat">
                <div className="stat-value">{typingData.errors}</div>
                <div>Errors</div>
              </div>
            </div>

            <div className="pass-criteria">
              <h3>Pass Criteria</h3>
              <ul>
                <li className={finalAccuracy >= 80 ? 'passed' : 'failed'}>
                  {finalAccuracy >= 80 ? '✅ Accuracy 80%+' : '❌ Accuracy below 80%'}
                </li>
              </ul>
            </div>

            <div className="results-actions">
              {finalAccuracy >= 80 ? (
                <button
                  className="btn btn-primary"
                  onClick={() => {
                    const nextLessonId = parseInt(id) + 1;
                    const nextExists = (lessons.hebrew || []).some((l) => l.id === nextLessonId);
                    if (nextExists) {
                      navigate(`/translated-hebrew-lesson/${nextLessonId}`);
                    } else {
                      navigate('/translated-hebrew-lessons');
                    }
                  }}
                >
                  {(() => {
                    const nextLessonId = parseInt(id) + 1;
                    const nextExists = (lessons.hebrew || []).some((l) => l.id === nextLessonId);
                    return nextExists ? 'Next Lesson' : 'Back to Lessons';
                  })()}
                </button>
              ) : (
                <button className="btn btn-primary" onClick={restartLesson}>
                  Try Again
                </button>
              )}
              <button className="btn btn-secondary" onClick={() => navigate('/translated-hebrew-lessons')}>
                Back to Lessons
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="lesson-content" dir="ltr">
      <div className="lesson-container">
        <div className="lesson-header">
          {(() => {
            const keysText = (currentLesson.keys || []).join(' ');
            const titleEn = `Lesson ${currentLesson.id}: ${keysText}`;
            const descEn = `Practice letters: ${keysText}`;
            const fingerEn = `Place your fingers on the keyboard for: ${keysText}`;
            return (
              <>
                <h1>{titleEn}</h1>
                <p>{descEn}</p>
                <div className="lesson-description">
                  <h4>Finger Position</h4>
                  <p>{fingerEn}</p>
                </div>
              </>
            );
          })()}
        </div>

        <div className="stats-grid">
          <div className="stat-card">
            <h3>{calculateProgress()}%</h3>
            <p>Completed</p>
          </div>
          <div className="stat-card">
            <h3>{calculateCPM()}</h3>
            <p>CPM</p>
          </div>
          <div className="stat-card">
            <h3>{calculateAccuracy()}%</h3>
            <p>Accuracy</p>
          </div>
          <div className="stat-card">
            <h3>{typingData.errors}</h3>
            <p>Errors</p>
          </div>
        </div>

        <div className="typing-area">
          <div className="text-display">
            {activeText.split('').map((char, index) => (
              <span
                key={index}
                className={`char ${index < currentCharIndex ? 'correct' : index === currentCharIndex ? 'current' : ''}`}
              >
                {index === currentCharIndex && <span className="current-char">{char}</span>}
                {index !== currentCharIndex && char}
              </span>
            ))}
          </div>

          <div className="typing-input-container">
            <input
              ref={inputRef}
              type="text"
              value={inputValue}
              onChange={handleInputChange}
              onKeyDown={handleKeyDown}
              onKeyUp={handleKeyUp}
              placeholder={'Type here'}
              disabled={!isActive && currentCharIndex > 0}
              className="typing-input"
            />
          </div>
        </div>

        <div className="control-buttons">
          {!isActive && currentCharIndex === 0 ? (
            <button
              className="control-btn"
              onClick={() => {
                setIsActive(true);
                setStartTime(Date.now());
                setTypingData((prev) => ({ ...prev, startTime: Date.now() }));
                inputRef.current?.focus();
              }}
            >
              Start Practice
            </button>
          ) : (
            <button className="control-btn secondary" onClick={() => setIsActive(false)}>
              Pause
            </button>
          )}
          <button className="control-btn secondary" onClick={restartLesson}>
            Restart
          </button>
          <button className="control-btn secondary" onClick={() => navigate('/translated-hebrew-lessons')}>
            Back to Lessons
          </button>
        </div>

        <div className="keyboard-section">
          <Keyboard
            targetKeys={getCurrentKeys()}
            currentKey={getCurrentKey()}
            overrideLanguage="hebrew"
            guideLanguage="english"
          />
        </div>
        {/* The Keyboard component renders the standard finger guide under the keyboard, same as regular lessons */}
      </div>
    </div>
  );
};

export default TranslatedHebrewLesson;
