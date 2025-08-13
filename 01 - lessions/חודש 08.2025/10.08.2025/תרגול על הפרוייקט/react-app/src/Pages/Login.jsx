import React, { useState } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Paper, 
  TextField, 
  Button, 
  Alert
} from '@mui/material';
import { Link, useNavigate } from 'react-router-dom';
import { useUser } from '../Contexts/UserContext';

const Login = () => {
  const [formData, setFormData] = useState({
    user_email: "",
    user_password: ""
  });
  const { login, loading, error, clearError } = useUser();
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    clearError();
    
    try {
      await login(formData);
      navigate('/');
    } catch (error) {
      // השגיאה כבר מטופלת בקונטקסט
    }
  };

  return (
    <Container maxWidth="sm" sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center',
      minHeight: '80vh',
      justifyContent: 'center'
    }}>
      <Box sx={{ 
        width: '100%', 
        maxWidth: 500,
        textAlign: 'center'
      }}>
        <Typography 
          variant="h2" 
          component="h1" 
          gutterBottom
          sx={{ 
            mb: 4,
            fontWeight: 'bold',
            color: 'primary.main'
          }}
        >
          התחברות
        </Typography>
        
        <Paper 
          elevation={3} 
          sx={{ 
            p: 4, 
            borderRadius: 3,
            backgroundColor: 'background.paper'
          }}
        >
          <Typography 
            variant="h4" 
            component="h2" 
            gutterBottom
            sx={{ 
              mb: 3,
              fontWeight: '600'
            }}
          >
            התחבר לחשבון שלך
          </Typography>
          
          {error && (
            <Alert severity="error" sx={{ mb: 3, borderRadius: 2 }}>
              {error}
            </Alert>
          )}
          
          <Box component="form" onSubmit={handleLogin} sx={{ mt: 2 }}>
            <TextField
              fullWidth
              label="אימייל"
              name="user_email"
              type="email"
              value={formData.user_email}
              onChange={handleChange}
              margin="normal"
              required
              variant="outlined"
              sx={{ mb: 2 }}
              disabled={loading}
            />
            
            <TextField
              fullWidth
              label="סיסמה"
              name="user_password"
              type="password"
              value={formData.user_password}
              onChange={handleChange}
              margin="normal"
              required
              variant="outlined"
              sx={{ mb: 3 }}
              disabled={loading}
            />
            
            <Button
              type="submit"
              fullWidth
              variant="contained"
              disabled={loading}
              sx={{ 
                mt: 2, 
                mb: 3,
                py: 1.5,
                borderRadius: 2,
                fontSize: '1.1rem',
                fontWeight: 'bold'
              }}
              size="large"
            >
              {loading ? 'מתחבר...' : 'התחבר'}
            </Button>
            
            <Box sx={{ textAlign: 'center' }}>
              <Typography variant="body1" sx={{ fontSize: '1rem' }}>
                אין לך חשבון?{' '}
                <Link 
                  to="/register" 
                  style={{ 
                    color: 'inherit', 
                    textDecoration: 'none',
                    fontWeight: 'bold',
                    color: '#1976d2'
                  }}
                >
                  הירשם כאן
                </Link>
              </Typography>
            </Box>
          </Box>
        </Paper>
      </Box>
    </Container>
  );
};

export default Login;
