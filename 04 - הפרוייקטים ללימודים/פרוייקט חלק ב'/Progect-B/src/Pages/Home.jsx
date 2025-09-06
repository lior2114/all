import React from 'react';
import { Box, Container, Typography, Button, Paper, Grid } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { Flight, Person, Star } from '@mui/icons-material';
import { useUi } from '../Contexts/UiContext';
import { UseUser } from '../Contexts/UserContexts';

export function Home() {
  const navigate = useNavigate();
  const { language } = useUi();
  const { isAuthenticated } = UseUser();
  const t = (he, en) => (language === 'he' ? he : en);

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, mb: 6, mx: 'auto', maxWidth: 1200 }}>
        {/* Hero Section */}
        <Paper elevation={3} sx={{ p: 6, borderRadius: 2, textAlign: 'center', mb: 4, mx: 'auto', maxWidth: 900 }}>
          <Typography variant="h2" component="h1" gutterBottom sx={{ color: 'primary.main', mb: 3 }}>
            {t('🌴 ברוכים הבאים למערכת החופשות', '🌴 Welcome to the Vacations System')}
          </Typography>
          
          <Typography variant="h5" component="h2" gutterBottom sx={{ mb: 4, color: 'text.secondary' }}>
            {t('מערכת לניהול חופשות מתקדמת', 'An advanced vacation management system')}
          </Typography>
          
          <Typography variant="body1" sx={{ mb: 6, fontSize: '1.1rem', maxWidth: 600, mx: 'auto' }}>
            {t('כאן תוכלו לראות חופשות, להירשם למערכת, ולהתחבר לחשבון שלכם', 'Here you can view vacations, register, and log in to your account')}
          </Typography>
          
          <Box sx={{ display: 'flex', gap: 2, justifyContent: 'center', flexWrap: 'wrap' }}>
            {!isAuthenticated && (
              <>
                <Button 
                  variant="contained" 
                  size="large" 
                  onClick={() => navigate('/register')}
                  sx={{ px: 4, py: 1.5 }}
                >
                  {t('הרשמה למערכת', 'Register')}
                </Button>
                
                <Button 
                  variant="outlined" 
                  size="large" 
                  onClick={() => navigate('/login')}
                  sx={{ px: 4, py: 1.5 }}
                >
                  {t('התחברות', 'Login')}
                </Button>
              </>
            )}
            
            <Button 
              variant="outlined" 
              size="large" 
              onClick={() => navigate('/vacations')}
              sx={{ px: 4, py: 1.5 }}
            >
              {t('צפה בחופשות', 'Browse Vacations')}
            </Button>
          </Box>
        </Paper>

        {/* Features Section */}
        <Grid container spacing={{ xs: 2, md: 3 }} className="home-features" justifyContent="center">
          <Grid item xs={12} md={4} sx={{ display: 'flex' }}>
            <Paper elevation={2} sx={{ p: 4, textAlign: 'center', height: '100%', width: '100%', maxWidth: 380, mx: 'auto' }}>
              <Flight sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h5" component="h3" gutterBottom>
                {t('חופשות מרהיבות', 'Stunning Vacations')}
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {t('גלה חופשות מדהימות ברחבי העולם עם מחירים משתלמים', 'Discover amazing vacations worldwide at great prices')}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4} sx={{ display: 'flex' }}>
            <Paper elevation={2} sx={{ p: 4, textAlign: 'center', height: '100%', width: '100%', maxWidth: 380, mx: 'auto' }}>
              <Person sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h5" component="h3" gutterBottom>
                {t('ניהול חשבון', 'Account Management')}
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {t('ניהול אישי של החשבון שלך עם היסטוריית הזמנות', 'Manage your account with order history')}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4} sx={{ display: 'flex' }}>
            <Paper elevation={2} sx={{ p: 4, textAlign: 'center', height: '100%', width: '100%', maxWidth: 380, mx: 'auto' }}>
              <Star sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h5" component="h3" gutterBottom>
                {t('חוות דעת', 'Reviews')}
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {t('קרא חוות דעת אמיתיות ממטיילים אחרים', 'Read real reviews from other travelers')}
              </Typography>
            </Paper>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}