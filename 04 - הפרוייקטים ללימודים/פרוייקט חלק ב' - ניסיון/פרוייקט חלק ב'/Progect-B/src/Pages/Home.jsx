import React from 'react';
import { Box, Container, Typography, Button, Paper, Grid } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { Flight, Person, Star } from '@mui/icons-material';
import { useUi } from '../Contexts/UiContext';
import { UseUser } from '../Contexts/UserContexts';
import styles from './Home.module.css';

export function Home() {
  const navigate = useNavigate();
  const { language } = useUi();
  const { isAuthenticated } = UseUser();
  const t = (he, en) => (language === 'he' ? he : en);

  return (
    <Container maxWidth="lg">
      <Box className={styles.homeContainer}>
        {/* Hero Section */}
        <Paper elevation={3} className={styles.heroSection}>
          <Typography variant="h2" component="h1" gutterBottom className={styles.heroTitle}>
            {t('🌴 ברוכים הבאים למערכת החופשות', '🌴 Welcome to the Vacations System')}
          </Typography>
          
          <Typography variant="h5" component="h2" gutterBottom className={styles.heroSubtitle}>
            {t('מערכת לניהול חופשות מתקדמת', 'An advanced vacation management system')}
          </Typography>
          
          <Typography variant="body1" className={styles.heroDescription}>
            {t('כאן תוכלו לראות חופשות, להירשם למערכת, ולהתחבר לחשבון שלכם', 'Here you can view vacations, register, and log in to your account')}
          </Typography>
          
          <Box className={styles.heroButtons}>
            {!isAuthenticated && (
              <>
                <Button 
                  variant="contained" 
                  size="large" 
                  onClick={() => navigate('/register')}
                  className={styles.heroButton}
                >
                  {t('הרשמה למערכת', 'Register')}
                </Button>
                
                <Button 
                  variant="outlined" 
                  size="large" 
                  onClick={() => navigate('/login')}
                  className={styles.heroButton}
                >
                  {t('התחברות', 'Login')}
                </Button>
              </>
            )}
            
            <Button 
              variant="outlined" 
              size="large" 
              onClick={() => navigate('/vacations')}
              className={styles.heroButton}
            >
              {t('צפה בחופשות', 'Browse Vacations')}
            </Button>
          </Box>
        </Paper>

        {/* Features Section */}
        <Grid container spacing={{ xs: 2, md: 3 }} className={styles.featuresSection} justifyContent="center">
          <Grid item xs={12} md={4} className={styles.featureGridItem}>
            <Paper elevation={2} className={styles.featureCard}>
              <Flight className={styles.featureIcon} />
              <Typography variant="h5" component="h3" gutterBottom className={styles.featureTitle}>
                {t('חופשות מרהיבות', 'Stunning Vacations')}
              </Typography>
              <Typography variant="body1" className={styles.featureDescription}>
                {t('גלה חופשות מדהימות ברחבי העולם עם מחירים משתלמים', 'Discover amazing vacations worldwide at great prices')}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4} className={styles.featureGridItem}>
            <Paper elevation={2} className={styles.featureCard}>
              <Person className={styles.featureIcon} />
              <Typography variant="h5" component="h3" gutterBottom className={styles.featureTitle}>
                {t('ניהול חשבון', 'Account Management')}
              </Typography>
              <Typography variant="body1" className={styles.featureDescription}>
                {t('ניהול אישי של החשבון שלך עם היסטוריית הזמנות', 'Manage your account with order history')}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4} className={styles.featureGridItem}>
            <Paper elevation={2} className={styles.featureCard}>
              <Star className={styles.featureIcon} />
              <Typography variant="h5" component="h3" gutterBottom className={styles.featureTitle}>
                {t('חוות דעת', 'Reviews')}
              </Typography>
              <Typography variant="body1" className={styles.featureDescription}>
                {t('קרא חוות דעת אמיתיות ממטיילים אחרים', 'Read real reviews from other travelers')}
              </Typography>
            </Paper>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
}