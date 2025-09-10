import React, { useEffect, useState } from 'react';
import { Container, Box, Paper, Typography, Avatar, Divider, Grid, Alert } from '@mui/material';
import { UseUser } from '../Contexts/UserContexts';
import { useNavigate } from 'react-router-dom';
import { useUi } from '../Contexts/UiContext';
import { getLikes, getVacations } from '../api/api';
import styles from './Profile.module.css';

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
    <Container maxWidth="md" className={styles.profileContainer}>
      <Box sx={{ mt: 4 }}>
        <Paper elevation={3} className={styles.profilePaper}>
          <Box className={styles.profileHeader}>
            <Avatar className={styles.profileAvatar}>
              {user?.first_name?.charAt(0) || 'U'}
            </Avatar>
            <Box className={styles.profileInfo}>
              <Typography variant="h5" className={styles.profileName}>
                {user?.first_name} {user?.last_name}
              </Typography>
              <Typography variant="body2" className={styles.profileEmail}>
                {user?.user_email}
              </Typography>
            </Box>
          </Box>

          <Divider className={styles.profileDivider} />

          <Typography variant="h6" className={styles.likedVacationsTitle}>
            {language === 'he' ? 'חופשות שאהבת' : 'Liked Vacations'}
          </Typography>

          {error && <Alert severity="error" className={styles.errorAlert}>{error}</Alert>}

          <Grid container spacing={2} className={styles.likedVacationsGrid}>
            {liked.map(v => (
              <Grid item xs={12} sm={6} md={4} key={v.vacation_id}>
                <Paper className={styles.likedVacationCard}>
                  <Typography variant="subtitle1" className={styles.likedVacationTitle}>{v.country_name}</Typography>
                  <Typography variant="body2" className={styles.likedVacationDescription}>{v.vacation_description}</Typography>
                </Paper>
              </Grid>
            ))}
            {liked.length === 0 && !error && (
              <Grid item xs={12}>
                <Typography variant="body2" className={styles.emptyState}>
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
