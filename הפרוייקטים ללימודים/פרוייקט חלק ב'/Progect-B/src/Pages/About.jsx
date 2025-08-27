import React from 'react';
import { Box, Container, Typography, Paper, Grid } from '@mui/material';
import { Flight, Security, Support } from '@mui/icons-material';
import { useUi } from '../Contexts/UiContext';

export function About() {
  const { language } = useUi();
  const t = (he, en) => (language === 'he' ? he : en);
  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, mb: 6, mx: 'auto', maxWidth: 1200 }}>
        {/* Hero Section */}
        <Paper elevation={3} sx={{ p: 6, borderRadius: 2, textAlign: 'center', mb: 4, mx: 'auto', maxWidth: 900 }}>
          <Typography variant="h2" component="h1" gutterBottom sx={{ color: 'primary.main', mb: 3 }}>
            {t('אודות מערכת החופשות', 'About the Vacations System')}
          </Typography>
          
          <Typography variant="h5" component="h2" gutterBottom sx={{ mb: 4, color: 'text.secondary' }}>
            {t('המערכת המתקדמת ביותר לניהול חופשות', 'The most advanced system for managing vacations')}
          </Typography>
          
          <Typography variant="body1" sx={{ mb: 4, fontSize: '1.1rem', maxWidth: 800, mx: 'auto' }}>
            {t('אנחנו מספקים פלטפורמה מתקדמת וידידותית למשתמש לניהול חופשות. המערכת שלנו מאפשרת לכם לגלות חופשות מדהימות, לנהל את החשבון שלכם ולקבל את השירות הטוב ביותר.', 'We provide an advanced and user-friendly platform for managing vacations. Our system allows you to discover amazing vacations, manage your account, and get the best service.')}
          </Typography>
        </Paper>

        {/* Features Section */}
        <Grid container spacing={{ xs: 2, md: 3 }} className="about-features" justifyContent="center">
          <Grid item xs={12} md={4} sx={{ display: 'flex' }}>
            <Paper elevation={2} sx={{ p: 4, textAlign: 'center', height: '100%', width: '100%', maxWidth: 380, mx: 'auto' }}>
              <Flight sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h5" component="h3" gutterBottom>
                {t('חופשות איכותיות', 'Quality Vacations')}
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {t('אנו מציעים מגוון רחב של חופשות איכותיות במחירים תחרותיים לכל הקהל', 'We offer a wide range of quality vacations at competitive prices for everyone')}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4} sx={{ display: 'flex' }}>
            <Paper elevation={2} sx={{ p: 4, textAlign: 'center', height: '100%', width: '100%', maxWidth: 380, mx: 'auto' }}>
              <Security sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h5" component="h3" gutterBottom>
                {t('אבטחת מידע', 'Data Security')}
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {t('המערכת שלנו מוגנת ברמה הגבוהה ביותר כדי להבטיח את אבטחת הנתונים שלכם', 'Our system is protected at the highest level to ensure your data security')}
              </Typography>
            </Paper>
          </Grid>
          
          <Grid item xs={12} md={4} sx={{ display: 'flex' }}>
            <Paper elevation={2} sx={{ p: 4, textAlign: 'center', height: '100%', width: '100%', maxWidth: 380, mx: 'auto' }}>
              <Support sx={{ fontSize: 60, color: 'primary.main', mb: 2 }} />
              <Typography variant="h5" component="h3" gutterBottom>
                {t('תמיכה 24/7', 'Support 24/7')}
              </Typography>
              <Typography variant="body1" color="text.secondary">
                {t('צוות התמיכה שלנו זמין לכם 24 שעות ביממה לכל שאלה או בעיה', 'Our support team is available 24/7 for any question or issue')}
              </Typography>
            </Paper>
          </Grid>
        </Grid>

        {/* Additional Info */}
        <Paper elevation={2} sx={{ p: 4, mt: 4, mx: 'auto', maxWidth: 900 }}>
          <Typography variant="h5" component="h3" gutterBottom sx={{ color: 'primary.main' }}>
            {t('המטרה שלנו', 'Our Goal')}
          </Typography>
          <Typography variant="body1" paragraph>
            {t('המטרה שלנו היא לספק לכם את החוויה הטובה ביותר בתכנון ובזמינות החופשות שלכם. אנחנו מאמינים שכל אחד ראוי לחופשה מושלמת, ואנחנו כאן כדי לעזור לכם להגשים את החלום הזה.', 'Our goal is to provide you with the best experience in planning and accessing your vacations. We believe everyone deserves the perfect vacation, and we are here to help you make that dream come true.')}
          </Typography>
          <Typography variant="body1">
            {t('המערכת שלנו פותחה על ידי צוות מקצועי של מפתחים ומומחי תיירות, כדי להבטיח שתקבלו את השירות הטוב והמהיר ביותר.', 'Our system was developed by a professional team of developers and tourism experts to ensure you receive the best and fastest service.')}
          </Typography>
        </Paper>
      </Box>
    </Container>
  );
}