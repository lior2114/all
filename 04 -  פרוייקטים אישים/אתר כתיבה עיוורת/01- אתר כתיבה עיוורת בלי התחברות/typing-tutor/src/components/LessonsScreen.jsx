import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useLanguage } from '../contexts/LanguageContext';
import { lessons } from '../data/lessons';
import './LessonsScreen.css';

const LessonsScreen = () => {
  const navigate = useNavigate();
  const { texts, language, isRTL } = useLanguage();
  const currentLessons = lessons[language] || lessons.hebrew;

  const calculateProgress = () => {
    const completed = currentLessons.filter(lesson => lesson.completed).length;
    return Math.round((completed / currentLessons.length) * 100);
  };

  const handleLessonClick = (lesson) => {
    if (!lesson.locked) {
      navigate(`/lesson/${lesson.id}`);
    }
  };

  return (
    <div className="lessons-screen" dir={isRTL ? 'rtl' : 'ltr'}>
      <div className="lessons-container">
        <div className="lessons-header">
          <h1>{texts.lessons}</h1>
          <p>{texts.overallProgress}: <span className="progress-percent">{calculateProgress()}%</span></p>
        </div>
        
        <div className="lessons-grid">
          {Object.entries(currentLessons.reduce((acc, l) => {
            const key = l.group || (language === 'hebrew' ? 'כללי' : 'General');
            if (!acc[key]) acc[key] = [];
            acc[key].push(l);
            return acc;
          }, {})).map(([group, list]) => (
            <div key={group} className="lesson-group">
              <h2 className="lesson-group-title">{group}</h2>
              <div className="lesson-group-grid">
                {list.map((lesson) => (
                  <div 
                    key={lesson.id}
                    className={`lesson-card ${lesson.completed ? 'completed' : ''} ${lesson.locked ? 'locked' : ''}`}
                  >
                    <div className="lesson-progress">
                      {lesson.completed ? '✓' : lesson.id}
                    </div>
                    <h3>{lesson.title}</h3>
                    <p className="lesson-description">{lesson.description}</p>
                    <div className="lesson-keys">
                      {lesson.keys.map((key, index) => (
                        <span key={index} className="lesson-key">{key}</span>
                      ))}
                    </div>
                    <div className="lesson-finger-guide">
                      <h4>{texts.fingerPosition}</h4>
                      <p>{lesson.fingerGuide}</p>
                    </div>
                    <button 
                      className="start-lesson-btn"
                      onClick={() => handleLessonClick(lesson)}
                      disabled={lesson.locked}
                    >
                      {lesson.locked ? (language === 'hebrew' ? '🔒 נעול' : '🔒 Locked') : texts.startPractice}
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

export default LessonsScreen; 