import React from 'react';
import { Container, Typography, Box, Paper } from '@mui/material';

const Home = () => {
  return (
    <Container maxWidth="lg" sx={{ 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center',
      minHeight: '80vh',
      justifyContent: 'center'
    }}>
      <Box sx={{ 
        width: '100%', 
        maxWidth: 800,
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
          ברוכים הבאים
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
            דף הבית
          </Typography>
          
          <Typography 
            variant="body1" 
            paragraph
            sx={{ 
              fontSize: '1.1rem',
              lineHeight: 1.8,
              mb: 2
            }}
          >
            זהו דף הבית של האפליקציה שלנו. כאן תוכלו למצוא מידע על השירותים שלנו
            ולגלול בין האפשרויות השונות.
          </Typography>
          
          <Typography 
            variant="body1"
            sx={{ 
              fontSize: '1rem',
              color: 'text.secondary'
            }}
          >
            השתמשו בתפריט הניווט למעלה כדי לנווט בין הדפים השונים.
          </Typography>
        </Paper>
      </Box>
    </Container>
  );
};

export default Home;
