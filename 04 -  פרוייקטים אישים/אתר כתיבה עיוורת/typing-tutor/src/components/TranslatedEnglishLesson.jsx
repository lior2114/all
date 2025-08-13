import React, { useEffect, useRef, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { lessons } from '../data/lessons';
import Keyboard from './Keyboard';
import './LessonContent.css';

const TranslatedEnglishLesson = () => {
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
    const lesson = (lessons.english || []).find((l) => l.id === lessonId);
    if (!lesson) {
      navigate('/translated-english-lessons');
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
      navigate('/translated-english-lessons');
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
    return <div>טוען...</div>;
  }

  if (isCompleted) {
    const finalCPM = calculateCPM();
    const finalAccuracy = calculateAccuracy();
    const timeElapsed = endTime && startTime ? Math.round((endTime - startTime) / 1000) : 0;

    return (
      <div className="lesson-content" dir="rtl">
        <div className="lesson-container">
          <div className="lesson-results card">
            <h2>{finalAccuracy >= 80 ? 'עברתם את השיעור!' : 'לא עמדתם בדרישות'}</h2>

            <div className="results-stats">
              <div className="result-stat">
                <div className="stat-value">{finalCPM}</div>
                <div>תווים בדקה</div>
              </div>
              <div className="result-stat">
                <div className="stat-value">{finalAccuracy}%</div>
                <div>דיוק</div>
              </div>
              <div className="result-stat">
                <div className="stat-value">{timeElapsed}s</div>
                <div>זמן</div>
              </div>
              <div className="result-stat">
                <div className="stat-value">{typingData.errors}</div>
                <div>שגיאות</div>
              </div>
            </div>

            <div className="pass-criteria">
              <h3>קריטריוני מעבר</h3>
              <ul>
                <li className={finalAccuracy >= 80 ? 'passed' : 'failed'}>
                  {finalAccuracy >= 80 ? '✅ דיוק 80% ומעלה' : '❌ דיוק מתחת ל-80%'}
                </li>
              </ul>
            </div>

            <div className="results-actions">
              {finalAccuracy >= 80 ? (
                <button className="btn btn-primary" onClick={() => navigate('/translated-english-lessons')}>
                  חזרה לשיעורים
                </button>
              ) : (
                <button className="btn btn-primary" onClick={restartLesson}>
                  נסו שוב
                </button>
              )}
              <button className="btn btn-secondary" onClick={() => navigate('/translated-english-lessons')}>
                חזרה לשיעורים
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="lesson-content" dir="rtl">
      <div className="lesson-container">
        <div className="lesson-header">
          {(() => {
            const keysText = (currentLesson.keys || []).join(' ');
            const titleHe = `שיעור ${currentLesson.id}: ${keysText}`;
            const descHe = `תרגול אותיות: ${keysText}`;
            const fingerHe = `מקמו את האצבעות בהתאם על המקלדת לאותיות: ${keysText}`;
            return (
              <>
                <h1>{titleHe}</h1>
                <p>{descHe}</p>
                <div className="lesson-description">
                  <h4>מיקום אצבעות</h4>
                  <p>{fingerHe}</p>
                </div>
              </>
            );
          })()}
        </div>

        <div className="stats-grid">
          <div className="stat-card">
            <h3>{calculateProgress()}%</h3>
            <p>הושלם</p>
          </div>
          <div className="stat-card">
            <h3>{calculateCPM()}</h3>
            <p>תווים בדקה</p>
          </div>
          <div className="stat-card">
            <h3>{calculateAccuracy()}%</h3>
            <p>דיוק</p>
          </div>
          <div className="stat-card">
            <h3>{typingData.errors}</h3>
            <p>שגיאות</p>
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
              placeholder={'הקלידו כאן'}
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
              התחלת תרגול
            </button>
          ) : (
            <button className="control-btn secondary" onClick={() => setIsActive(false)}>
              השהה
            </button>
          )}
          <button className="control-btn secondary" onClick={restartLesson}>
            אתחל
          </button>
          <button className="control-btn secondary" onClick={() => navigate('/translated-english-lessons')}>
            חזרה לשיעורים
          </button>
        </div>

        <div className="keyboard-section">
          <Keyboard
            targetKeys={getCurrentKeys()}
            currentKey={getCurrentKey()}
            overrideLanguage="english"
            guideLanguage="hebrew"
          />
        </div>
        {/* The Keyboard component renders the standard finger guide under the keyboard, same as regular lessons */}
      </div>
    </div>
  );
};

export default TranslatedEnglishLesson;
