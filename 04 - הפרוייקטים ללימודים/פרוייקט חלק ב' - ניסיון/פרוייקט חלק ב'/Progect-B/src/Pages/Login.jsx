import React, { useState } from 'react';
import {
  Box,
  Container,
  Paper,
  TextField,
  Button,
  Typography,
  Alert,
  CircularProgress,
  InputAdornment,
  IconButton
} from '@mui/material';
import {
  Visibility,
  VisibilityOff,
  Email,
  Lock
} from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';
import { UseUser } from '../Contexts/UserContexts';
import { useUi } from '../Contexts/UiContext';
import styles from './Login.module.css';

export function Login() {
  const navigate = useNavigate();
  const { login, loading, error, clearError } = UseUser();
  const { language } = useUi();
  const t = (he, en) => (language === 'he' ? he : en);
  
  const [formData, setFormData] = useState({
    user_email: '',
    user_password: ''
  });
  
  const [errors, setErrors] = useState({});
  const [showPassword, setShowPassword] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
    
    // Clear previous error for this field
    setErrors(prev => ({ ...prev, [name]: '' }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    clearError();
    
    // Basic validation
    const newErrors = {};
    if (!formData.user_email.trim()) {
      newErrors.user_email = 'אימייל הוא שדה חובה';
    }
    if (!formData.user_password) {
      newErrors.user_password = 'סיסמה היא שדה חובה';
    }
    
    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }
    
    try {
      await login(formData);
      navigate('/vacations'); // Navigate to vacations page after successful login
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <Container component="main" maxWidth="sm">
      <Box className={styles.loginContainer}>
        <Paper elevation={3} className={styles.loginPaper}>
          <Typography component="h1" variant="h4" className={styles.loginTitle}>
            {t('התחברות למערכת', 'Login')}
          </Typography>
          
          {error && (
            <Alert severity="error" className={styles.errorAlert}>
              {error}
            </Alert>
          )}
          
          <Box component="form" onSubmit={handleSubmit} className={styles.loginForm}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="user_email"
              label={t('אימייל', 'Email')}
              name="user_email"
              autoComplete="email"
              type="email"
              autoFocus
              value={formData.user_email}
              onChange={handleInputChange}
              error={!!errors.user_email}
              helperText={errors.user_email}
              className={styles.loginField}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <Email className={styles.inputAdornment} />
                  </InputAdornment>
                ),
              }}
              InputLabelProps={{ shrink: true }}
            />
            
            <TextField
              margin="normal"
              required
              fullWidth
              name="user_password"
              label={t('סיסמה', 'Password')}
              type={showPassword ? 'text' : 'password'}
              id="user_password"
              autoComplete="current-password"
              value={formData.user_password}
              onChange={handleInputChange}
              error={!!errors.user_password}
              helperText={errors.user_password}
              className={styles.loginField}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <Lock className={styles.inputAdornment} />
                  </InputAdornment>
                ),
                endAdornment: (
                  <InputAdornment position="end">
                    <IconButton
                      aria-label="toggle password visibility"
                      onClick={() => setShowPassword(!showPassword)}
                      edge="end"
                    >
                      {showPassword ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                ),
              }}
              InputLabelProps={{ shrink: true }}
            />
            
            <Button
              type="submit"
              fullWidth
              variant="contained"
              className={styles.loginButton}
              disabled={loading}
            >
              {loading ? (
                <CircularProgress size={24} color="inherit" />
              ) : (
                t('התחבר', 'Login')
              )}
            </Button>
            
            <Button
              fullWidth
              variant="text"
              onClick={() => navigate('/register')}
              className={styles.loginLink}
            >
              {t('אין לך חשבון? הירשם כאן', 'No account? Register here')}
            </Button>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
}