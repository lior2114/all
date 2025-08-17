import React, { useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import WelcomeScreen from './components/WelcomeScreen';
import LessonsScreen from './components/LessonsScreen';
import LessonContent from './components/LessonContent';
import TranslatedEnglishLessons from './components/TranslatedEnglishLessons';
import TranslatedEnglishLesson from './components/TranslatedEnglishLesson';
import TranslatedHebrewLessons from './components/TranslatedHebrewLessons';
import TranslatedHebrewLesson from './components/TranslatedHebrewLesson';
import FreePractice from './components/FreePractice';
import RandomWordsTest from './components/RandomWordsTest';
import ResultsScreen from './components/ResultsScreen';
import Header from './components/Header';
import { LanguageProvider, useLanguage } from './contexts/LanguageContext';
import './App.css';

const AppContent = () => {
  const { darkMode } = useLanguage();

  useEffect(() => {
    document.documentElement.setAttribute('data-theme', darkMode ? 'dark' : 'light');
  }, [darkMode]);

  return (
    <div className="App">
      <Header />
      <Routes>
        <Route path="/" element={<WelcomeScreen />} />
        <Route path="/lessons" element={<LessonsScreen />} />
        <Route path="/lesson/:id" element={<LessonContent />} />
        <Route path="/translated-english-lessons" element={<TranslatedEnglishLessons />} />
        <Route path="/translated-english-lesson/:id" element={<TranslatedEnglishLesson />} />
        <Route path="/translated-hebrew-lessons" element={<TranslatedHebrewLessons />} />
        <Route path="/translated-hebrew-lesson/:id" element={<TranslatedHebrewLesson />} />
        <Route path="/free-practice" element={<FreePractice />} />
        <Route path="/random-words-test" element={<RandomWordsTest />} />
        <Route path="/results" element={<ResultsScreen />} />
      </Routes>
    </div>
  );
};

function App() {
  return (
    <LanguageProvider>
      <Router>
        <AppContent />
      </Router>
    </LanguageProvider>
  );
}

export default App; 