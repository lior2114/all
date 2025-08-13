import React, { useState } from 'react';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
  Avatar,
  Menu,
  MenuItem,
  IconButton,
  Badge
} from '@mui/material';
import { AdminPanelSettings } from '@mui/icons-material';
import { useNavigate, useLocation } from 'react-router-dom';
import { useUser } from '../../Contexts/UserContext';

const NavBar = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { user, logout } = useUser();
  const [anchorEl, setAnchorEl] = useState(null);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    logout();
    handleClose();
    navigate('/');
  };

  const handleProfile = () => {
    handleClose();
    navigate('/profile');
  };

  const handleAdmin = () => {
    handleClose();
    navigate('/admin');
  };

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <AppBar position="static" sx={{ backgroundColor: 'primary.main' }}>
      <Toolbar sx={{ justifyContent: 'space-between' }}>
        {/* צד ימין - ניווט ראשי */}
        <Box sx={{ display: 'flex', gap: 2 }}>
          <Button
            color="inherit"
            onClick={() => navigate('/')}
            sx={{
              fontWeight: isActive('/') ? 'bold' : 'normal',
              textDecoration: isActive('/') ? 'underline' : 'none'
            }}
          >
            דף הבית
          </Button>
          <Button
            color="inherit"
            onClick={() => navigate('/about')}
            sx={{
              fontWeight: isActive('/about') ? 'bold' : 'normal',
              textDecoration: isActive('/about') ? 'underline' : 'none'
            }}
          >
            אודות
          </Button>
          <Button
            color="inherit"
            onClick={() => navigate('/vacations')}
            sx={{
              fontWeight: isActive('/vacations') ? 'bold' : 'normal',
              textDecoration: isActive('/vacations') ? 'underline' : 'none'
            }}
          >
            חופשות
          </Button>
          <Button
            color="inherit"
            onClick={() => navigate('/statistics')}
            sx={{
              fontWeight: isActive('/statistics') ? 'bold' : 'normal',
              textDecoration: isActive('/statistics') ? 'underline' : 'none'
            }}
          >
            סטטיסטיקות
          </Button>
        </Box>

        {/* צד שמאל - כפתורי משתמש */}
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          {user ? (
            <>
              {/* כפתור אדמין */}
              {user.role_id === 1 && (
                <Button
                  color="inherit"
                  startIcon={<AdminPanelSettings />}
                  onClick={() => navigate('/admin')}
                  sx={{
                    fontWeight: isActive('/admin') ? 'bold' : 'normal',
                    textDecoration: isActive('/admin') ? 'underline' : 'none'
                  }}
                >
                  ניהול
                </Button>
              )}
              
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleMenu}
                color="inherit"
              >
                <Avatar 
                  sx={{ 
                    width: 32, 
                    height: 32, 
                    bgcolor: 'secondary.main',
                    backgroundImage: user.profile_image ? `url(${user.profile_image})` : 'none',
                    backgroundSize: 'cover',
                    backgroundPosition: 'center'
                  }}
                >
                  {!user.profile_image && (user.first_name?.charAt(0) || user.user_email?.charAt(0) || 'U')}
                </Avatar>
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorEl}
                anchorOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                keepMounted
                transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
                }}
                open={Boolean(anchorEl)}
                onClose={handleClose}
              >
                <MenuItem onClick={handleProfile}>פרופיל</MenuItem>
                {user.role_id === 1 && (
                  <MenuItem onClick={handleAdmin}>ניהול מערכת</MenuItem>
                )}
                <MenuItem onClick={handleLogout}>התנתק</MenuItem>
              </Menu>
            </>
          ) : (
            <>
              <Button
                color="inherit"
                onClick={() => navigate('/login')}
                sx={{
                  fontWeight: isActive('/login') ? 'bold' : 'normal',
                  textDecoration: isActive('/login') ? 'underline' : 'none'
                }}
              >
                התחבר
              </Button>
              <Button
                color="inherit"
                onClick={() => navigate('/register')}
                sx={{
                  fontWeight: isActive('/register') ? 'bold' : 'normal',
                  textDecoration: isActive('/register') ? 'underline' : 'none'
                }}
              >
                הרשמה
              </Button>
            </>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default NavBar;
