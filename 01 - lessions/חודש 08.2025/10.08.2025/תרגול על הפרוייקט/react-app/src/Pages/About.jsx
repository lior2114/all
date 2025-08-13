import React from 'react';
import { Container, Typography, Box, Paper, Grid, Card, CardContent } from '@mui/material';

const About = () => {
  return (
    <Container maxWidth="lg" sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center',
      minHeight: '80vh',
      py: 4
    }}>
      <Box sx={{ 
        width: '100%', 
        maxWidth: 1000,
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
          אודות
        </Typography>
        
        <Paper 
          elevation={3} 
          sx={{ 
            p: 4, 
            mb: 4,
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
            על הפרויקט
          </Typography>
          
          <Typography 
            variant="body1" 
            paragraph
            sx={{ 
              fontSize: '1.1rem',
              lineHeight: 1.8
            }}
          >
            זהו פרויקט React עם Material-UI שמציג מערכת ניהול חופשות.
            הפרויקט כולל מערכת הרשמה והתחברות, ניהול חופשות, וממשק משתמש מודרני.
          </Typography>
        </Paper>

        <Grid container spacing={3} justifyContent="center">
          <Grid size={{ xs: 12, md: 4 }}>
            <Card sx={{ 
              height: '100%', 
              display: 'flex', 
              flexDirection: 'column',
              borderRadius: 3,
              '&:hover': {
                transform: 'translateY(-5px)',
                transition: 'transform 0.3s ease-in-out'
              }
            }}>
              <CardContent sx={{ textAlign: 'center', p: 3 }}>
                <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold', color: 'primary.main' }}>
                  React
                </Typography>
                <Typography variant="body2" sx={{ fontSize: '1rem', lineHeight: 1.6 }}>
                  ספריית JavaScript לבניית ממשקי משתמש אינטראקטיביים
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          
          <Grid size={{ xs: 12, md: 4 }}>
            <Card sx={{ 
              height: '100%', 
              display: 'flex', 
              flexDirection: 'column',
              borderRadius: 3,
              '&:hover': {
                transform: 'translateY(-5px)',
                transition: 'transform 0.3s ease-in-out'
              }
            }}>
              <CardContent sx={{ textAlign: 'center', p: 3 }}>
                <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold', color: 'primary.main' }}>
                  Material-UI
                </Typography>
                <Typography variant="body2" sx={{ fontSize: '1rem', lineHeight: 1.6 }}>
                  ספריית רכיבי UI מודרנית המבוססת על עקרונות Material Design
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          
          <Grid size={{ xs: 12, md: 4 }}>
            <Card sx={{ 
              height: '100%', 
              display: 'flex', 
              flexDirection: 'column',
              borderRadius: 3,
              '&:hover': {
                transform: 'translateY(-5px)',
                transition: 'transform 0.3s ease-in-out'
              }
            }}>
              <CardContent sx={{ textAlign: 'center', p: 3 }}>
                <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold', color: 'primary.main' }}>
                  Vite
                </Typography>
                <Typography variant="body2" sx={{ fontSize: '1rem', lineHeight: 1.6 }}>
                  כלי בנייה מהיר ומודרני לפיתוח React
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default About;
