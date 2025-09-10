import React, { useState } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  IconButton,
  Box,
  Menu,
  MenuItem,
  Avatar,
  Divider,
  Tooltip,
  Switch
} from '@mui/material';
import {
  Menu as MenuIcon,
  Home as HomeIcon,
  Flight as FlightIcon,
  Person as PersonIcon,
  Login as LoginIcon,
  Logout as LogoutIcon,
  DarkMode as DarkModeIcon,
  LightMode as LightModeIcon,
  Translate as TranslateIcon,
  AdminPanelSettings as AdminPanelSettingsIcon
} from '@mui/icons-material';
import { useNavigate, useLocation } from 'react-router-dom';
import { UseUser } from '../Contexts/UserContexts';
import { useUi } from '../Contexts/UiContext';
import styles from './NavBar.module.css';

export function NavBar() {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, isAuthenticated, logout } = UseUser();
  const { language, mode, toggleLanguage, toggleMode } = useUi();
  
  const [anchorEl, setAnchorEl] = useState(null);
  const [mobileMenuAnchor, setMobileMenuAnchor] = useState(null);

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMobileMenuOpen = (event) => {
    setMobileMenuAnchor(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
    setMobileMenuAnchor(null);
  };

  const handleLogout = () => {
    logout();
    handleMenuClose();
    navigate('/');
  };

  const handleNavigation = (path) => {
    navigate(path);
    handleMenuClose();
  };

  const isActive = (path) => {
    return location.pathname === path;
  };

  const menuItems = [
    { text: language === 'he' ? 'בית' : 'Home', path: '/', icon: <HomeIcon /> },
    { text: language === 'he' ? 'חופשות' : 'Vacations', path: '/vacations', icon: <FlightIcon /> },
    { text: language === 'he' ? 'אודות' : 'About', path: '/about', icon: <PersonIcon /> }
  ];

  return (
    <AppBar position="static" className={styles.navBar}>
      <Toolbar className={styles.toolbar}>
        <Typography 
          variant="h6" 
          component="div" 
          className={styles.brandTitle}
          onClick={() => navigate('/')}
        >
          {language === 'he' ? '🌴 מערכת החופשות' : '🌴 Vacations System'}
        </Typography>

        <Box className={styles.desktopMenu}>
          {/* Theme toggle */}
          <Tooltip title={language === 'he' ? (mode === 'dark' ? 'מצב יום' : 'מצב לילה') : (mode === 'dark' ? 'Light mode' : 'Dark mode')}>
            <IconButton color="inherit" onClick={toggleMode}>
              {mode === 'dark' ? <LightModeIcon /> : <DarkModeIcon />}
            </IconButton>
          </Tooltip>

          {/* Language toggle */}
          <Tooltip title={language === 'he' ? 'החלף שפה' : 'Toggle language'}>
            <IconButton color="inherit" onClick={toggleLanguage}>
              <TranslateIcon />
            </IconButton>
          </Tooltip>

          {menuItems.map((item) => (
            <Button
              key={item.path}
              color="inherit"
              startIcon={item.icon}
              onClick={() => handleNavigation(item.path)}
              className={`${styles.menuButton} ${isActive(item.path) ? styles.menuButtonActive : ''}`}
            >
              {item.text}
            </Button>
          ))}

          {isAuthenticated && user?.role_id === 1 && (
            <Button
              color="inherit"
              startIcon={<AdminPanelSettingsIcon />}
              onClick={() => handleNavigation('/admin')}
              className={styles.menuButton}
            >
              {language === 'he' ? 'ניהול' : 'Admin'}
            </Button>
          )}
        </Box>

        <Box className={styles.userSection}>
          {isAuthenticated ? (
            <>
              <Button
                color="inherit"
                startIcon={<PersonIcon />}
                onClick={() => handleNavigation('/profile')}
                className={styles.userButton}
              >
                {user?.first_name || (language === 'he' ? 'משתמש' : 'User')}
              </Button>
              <IconButton color="inherit" onClick={handleLogout} title={language === 'he' ? 'התנתק' : 'Logout'}>
                <LogoutIcon />
              </IconButton>
            </>
          ) : (
            <>
              <Button
                color="inherit"
                startIcon={<LoginIcon />}
                onClick={() => navigate('/login')}
                className={styles.loginButton}
              >
                {language === 'he' ? 'התחברות' : 'Login'}
              </Button>
              <Button
                variant="contained"
                color="secondary"
                onClick={() => navigate('/register')}
                className={styles.registerButton}
              >
                {language === 'he' ? 'הרשמה' : 'Register'}
              </Button>
            </>
          )}
        </Box>

        {/* Mobile Menu Button */}
        <IconButton size="large" edge="end" color="inherit" aria-label="menu" onClick={handleMobileMenuOpen} className={styles.mobileMenuButton}>
          <MenuIcon />
        </IconButton>
      </Toolbar>

      {/* Profile Menu */}
      <Menu anchorEl={anchorEl} open={Boolean(anchorEl)} onClose={handleMenuClose} anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }} transformOrigin={{ vertical: 'top', horizontal: 'right' }} className={styles.profileMenu}>
        <MenuItem onClick={() => handleNavigation('/profile')}>
          <Box className={styles.profileMenuItem}>
            <Avatar className={styles.profileAvatar}>
              {user?.first_name?.charAt(0) || 'U'}
            </Avatar>
            <Box className={styles.profileInfo}>
              <Typography variant="body2" className={styles.profileName}>
                {user?.first_name} {user?.last_name}
              </Typography>
              <Typography variant="caption" className={styles.profileEmail}>
                {user?.user_email}
              </Typography>
            </Box>
          </Box>
        </MenuItem>
        <Divider />
        <MenuItem onClick={handleLogout}>
          <LogoutIcon sx={{ mr: 1 }} />
          {language === 'he' ? 'התנתק' : 'Logout'}
        </MenuItem>
      </Menu>

      {/* Mobile Menu */}
      <Menu anchorEl={mobileMenuAnchor} open={Boolean(mobileMenuAnchor)} onClose={handleMenuClose} anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }} transformOrigin={{ vertical: 'top', horizontal: 'right' }} className={styles.mobileMenu}>
        {[
          ...menuItems.map((item) => (
            <MenuItem key={item.path} onClick={() => handleNavigation(item.path)} selected={isActive(item.path)} className={styles.mobileMenuItem}>
              <Box className={styles.mobileMenuItem}>
                {item.icon}
                {item.text}
              </Box>
            </MenuItem>
          )),
          isAuthenticated && user?.role_id === 1 && (
            <MenuItem key="admin" onClick={() => handleNavigation('/admin')} className={styles.mobileMenuItem}>
              <Box className={styles.mobileMenuItem}>
                <AdminPanelSettingsIcon />
                {language === 'he' ? 'ניהול' : 'Admin'}
              </Box>
            </MenuItem>
          ),
          <Divider key="divider" />,
          ...(isAuthenticated ? [
            <MenuItem key="profile" onClick={() => handleNavigation('/profile')} className={styles.mobileMenuItem}>
              <Box className={styles.mobileMenuItem}>
                <PersonIcon />
                {user?.first_name || (language === 'he' ? 'משתמש' : 'User')}
              </Box>
            </MenuItem>,
            <MenuItem key="logout" onClick={handleLogout} className={styles.mobileMenuItem}>
              <Box className={styles.mobileMenuItem}>
                <LogoutIcon />
                {language === 'he' ? 'התנתק' : 'Logout'}
              </Box>
            </MenuItem>
          ] : [
            <MenuItem key="login" onClick={() => handleNavigation('/login')} className={styles.mobileMenuItem}>
              <Box className={styles.mobileMenuItem}>
                <LoginIcon />
                {language === 'he' ? 'התחברות' : 'Login'}
              </Box>
            </MenuItem>,
            <MenuItem key="register" onClick={() => handleNavigation('/register')} className={styles.mobileMenuItem}>
              <Box className={styles.mobileMenuItem}>
                <PersonIcon />
                {language === 'he' ? 'הרשמה' : 'Register'}
              </Box>
            </MenuItem>
          ])
        ]}
      </Menu>
    </AppBar>
  );
}
