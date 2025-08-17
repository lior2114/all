import React from 'react';
import { useNavigate } from 'react-router-dom';
import { lessons } from '../data/lessons';
import './LessonsScreen.css';

const TranslatedEnglishLessons = () => {
  const navigate = useNavigate();
  // In US->IL mode, hide lesson 15 as requested
  const englishLessons = (lessons.english || []).filter(l => l.id !== 15);

  const calculateProgress = () => {
    const completed = englishLessons.filter(lesson => lesson.completed).length;
    return Math.round((completed / (englishLessons.length || 1)) * 100);
    };

  const handleLessonClick = (lesson) => {
    if (!lesson.locked) {
      navigate(`/translated-english-lesson/${lesson.id}`);
    }
  };

  const grouped = englishLessons.reduce((acc, l) => {
    const key = l.group || 'כללי';
    if (!acc[key]) acc[key] = [];
    acc[key].push(l);
    return acc;
  }, {});

  const groupTitleHe = (group) => {
    const map = {
      'Index Finger': 'אצבע מורה',
      'Middle Finger': 'אצבע אמצעית',
      'Ring Finger': 'אצבע קמיצה',
      'Pinky': 'זרת',
      'General': 'כללי',
    };
    return map[group] || group || 'כללי';
  };

  const buildLessonTitleHe = (lesson) => {
    const keys = (lesson.keys || []).join(' ');
    return `שיעור ${lesson.id}: ${keys}`;
  };

  const buildDescriptionHe = (lesson) => {
    const keys = (lesson.keys || []).join(' ');
    return `תרגול אותיות: ${keys}`;
  };

  const buildFingerGuideHe = (lesson) => {
    const keys = (lesson.keys || []).join(' ');
    return `מקמו את האצבעות בהתאם על המקלדת לאותיות: ${keys}`;
  };

  return (
    <div className="lessons-screen" dir="rtl">
      <div className="lessons-container">
        <div className="lessons-header">
          <h1>שיעורי אנגלית מתורגמים</h1>
          <p>התקדמות כוללת: <span className="progress-percent">{calculateProgress()}%</span></p>
        </div>

        <div className="lessons-grid">
          {Object.entries(grouped).map(([group, list]) => (
            <div key={group} className="lesson-group">
              <h2 className="lesson-group-title">{groupTitleHe(group)}</h2>
              <div className="lesson-group-grid">
                {list.map((lesson) => (
                  <div 
                    key={lesson.id}
                    className={`lesson-card ${lesson.completed ? 'completed' : ''} ${lesson.locked ? 'locked' : ''}`}
                  >
                    <div className="lesson-progress">
                      {lesson.completed ? '✓' : lesson.id}
                    </div>
                    <h3>{buildLessonTitleHe(lesson)}</h3>
                    <p className="lesson-description">{buildDescriptionHe(lesson)}</p>
                    <div className="lesson-keys">
                      {lesson.keys.map((key, index) => (
                        <span key={index} className="lesson-key">{key}</span>
                      ))}
                    </div>
                    <div className="lesson-finger-guide">
                      <h4>מיקום אצבעות</h4>
                      <p>{buildFingerGuideHe(lesson)}</p>
                    </div>
                    <button 
                      className="start-lesson-btn"
                      onClick={() => handleLessonClick(lesson)}
                      disabled={lesson.locked}
                    >
                      {lesson.locked ? '🔒 נעול' : 'התחל תרגול'}
                    </button>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default TranslatedEnglishLessons;
