import React, { useEffect, useState } from 'react';
import { Container, Box, Paper, Typography, Avatar, Divider, Grid, Alert } from '@mui/material';
import { UseUser } from '../Contexts/UserContexts';
import { useNavigate } from 'react-router-dom';
import { useUi } from '../Contexts/UiContext';
import { getLikes, getVacations } from '../api/api';

export function Profile() {
  const { isAuthenticated, user } = UseUser();
  const { language } = useUi();
  const navigate = useNavigate();
  const [liked, setLiked] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login');
      return;
    }
    const fetchData = async () => {
      try {
        const [likesData, vacationsData] = await Promise.all([getLikes(), getVacations()]);
        const myLikes = Array.isArray(likesData)
          ? likesData.filter(l => Number(l.user_id) === Number(user.user_id))
          : [];
        const likedVacationIds = new Set(myLikes.map(m => Number(m.vacation_id)));
        const likedVacations = Array.isArray(vacationsData)
          ? vacationsData.filter(v => likedVacationIds.has(Number(v.vacation_id)))
          : [];
        setLiked(likedVacations);
      } catch (e) {
        setError(e.message || 'Failed to load profile');
      }
    };
    fetchData();
  }, [isAuthenticated, navigate, user]);

  return (
    <Container maxWidth="md">
      <Box sx={{ mt: 4 }}>
        <Paper elevation={3} sx={{ p: 4 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
            <Avatar sx={{ width: 56, height: 56 }}>
              {user?.first_name?.charAt(0) || 'U'}
            </Avatar>
            <Box>
              <Typography variant="h5" sx={{ fontWeight: 'bold' }}>
                {user?.first_name} {user?.last_name}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {user?.user_email}
              </Typography>
            </Box>
          </Box>

          <Divider sx={{ my: 2 }} />

          <Typography variant="h6" sx={{ mb: 2 }}>
            {language === 'he' ? 'חופשות שאהבת' : 'Liked Vacations'}
          </Typography>

          {error && <Alert severity="error">{error}</Alert>}

          <Grid container spacing={2}>
            {liked.map(v => (
              <Grid item xs={12} sm={6} md={4} key={v.vacation_id}>
                <Paper sx={{ p: 2 }}>
                  <Typography variant="subtitle1" sx={{ fontWeight: 'bold' }}>{v.country_name}</Typography>
                  <Typography variant="body2" color="text.secondary">{v.vacation_description}</Typography>
                </Paper>
              </Grid>
            ))}
            {liked.length === 0 && !error && (
              <Grid item xs={12}>
                <Typography variant="body2" color="text.secondary">
                  {language === 'he' ? 'אין חופשות שאהבת עדיין.' : 'No liked vacations yet.'}
                </Typography>
              </Grid>
            )}
          </Grid>
        </Paper>
      </Box>
    </Container>
  );
}
