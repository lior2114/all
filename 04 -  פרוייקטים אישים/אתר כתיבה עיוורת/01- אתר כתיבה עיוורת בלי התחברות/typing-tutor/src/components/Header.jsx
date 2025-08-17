import React, { useState, useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useLanguage } from '../contexts/LanguageContext';
import './Header.css';

const Header = () => {
  const { language, toggleLanguage, isRTL, darkMode, toggleDarkMode, texts } = useLanguage();
  const navigate = useNavigate();
  const location = useLocation();
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  // Update navLinks when language changes
  const navLinks = isRTL ? [
    { path: '/random-words-test', label: texts.randomWordsTest },
    { path: '/free-practice', label: texts.freePractice },
    { path: '/lessons', label: texts.lessons },
    { path: '/', label: texts.home }
  ] : [
    { path: '/', label: texts.home },
    { path: '/lessons', label: texts.lessons },
    { path: '/free-practice', label: texts.freePractice },
    { path: '/random-words-test', label: texts.randomWordsTest }
  ];

  const isActiveLink = (path) => {
    if (path === '/') {
      return location.pathname === '/';
    }
    return location.pathname.startsWith(path);
  };

  const handleNavigation = (path) => {
    navigate(path);
    setMobileMenuOpen(false);
  };

  const handleLanguageToggle = () => {
    toggleLanguage();
    // Close mobile menu when switching language
    setMobileMenuOpen(false);
  };

  // Close mobile menu when location changes
  useEffect(() => {
    setMobileMenuOpen(false);
  }, [location.pathname]);

  const isOnTranslated = (
    location.pathname.startsWith('/translated-english-') ||
    location.pathname.startsWith('/translated-hebrew-') ||
    location.pathname === '/translated-english-lessons' ||
    location.pathname === '/translated-hebrew-lessons'
  );

  // IL→US: English typing with Hebrew instructions → Translated English routes
  // US→IL: Hebrew typing with English instructions → Translated Hebrew routes
  const isEnTranslated = (
    location.pathname.startsWith('/translated-english-') ||
    location.pathname === '/translated-english-lessons'
  );
  const translatedDirection = isEnTranslated ? 'dir-il-to-us' : 'dir-us-to-il';

  return (
    <header className="header" dir={isRTL ? 'rtl' : 'ltr'}>
      <div className="header-content">
        <div className="logo" onClick={() => handleNavigation('/')}>
          <span className="logo-icon">⌨️</span>
          <span className="logo-text">{texts.title}</span>
        </div>

        <nav className="nav-menu">
          {navLinks.map((link) => (
            <button
              key={link.path}
              className={`nav-link ${isActiveLink(link.path) ? 'active' : ''}`}
              onClick={() => handleNavigation(link.path)}
            >
              {link.label}
            </button>
          ))}
        </nav>

        <div className="header-controls">
          {/* Translated mode toggle */}
          <button
            className={`dark-mode-toggle ${isOnTranslated ? `active ${translatedDirection}` : ''}`}
            onClick={() => {
              // Toggle between translated English and translated Hebrew routes
              const path = location.pathname;
              const onEnToHe = path.startsWith('/translated-english-') || path === '/translated-english-lessons';
              if (onEnToHe) {
                navigate('/translated-hebrew-lessons');
              } else {
                navigate('/translated-english-lessons');
              }
              setMobileMenuOpen(false);
            }}
            title={texts.translatedToggle}
          >
            <span className="toggle-icon">{isEnTranslated ? '🇮🇱➡️🇺🇸' : '🇺🇸➡️🇮🇱'}</span>
            <span>{texts.translatedToggle}</span>
          </button>

          <button
            className={`language-toggle ${language === 'hebrew' ? 'active' : ''}`}
            onClick={handleLanguageToggle}
          >
            <span className="toggle-icon">
              {language === 'hebrew' ? '🇮🇱' : '🇺🇸'}
            </span>
            <span>{language === 'hebrew' ? 'עברית' : 'English'}</span>
          </button>

          <button
            className={`dark-mode-toggle ${darkMode ? 'active' : ''}`}
            onClick={toggleDarkMode}
            title={darkMode ? 'Light Mode' : 'Dark Mode'}
          >
            <span className="toggle-icon">
              {darkMode ? '☀️' : '🌙'}
            </span>
            <span>{texts.darkMode}</span>
          </button>

          <button
            className="mobile-menu-toggle"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          >
            {mobileMenuOpen ? '✕' : '☰'}
          </button>
        </div>
      </div>

      <nav className={`mobile-menu ${mobileMenuOpen ? 'open' : ''}`}>
        {navLinks.map((link) => (
          <button
            key={link.path}
            className={`nav-link ${isActiveLink(link.path) ? 'active' : ''}`}
            onClick={() => handleNavigation(link.path)}
          >
            {link.label}
          </button>
        ))}
      </nav>
    </header>
  );
};

export default Header; 