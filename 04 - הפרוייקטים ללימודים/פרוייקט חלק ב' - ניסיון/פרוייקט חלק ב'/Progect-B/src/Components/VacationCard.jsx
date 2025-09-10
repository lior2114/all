import React from 'react';
import {
  Box,
  Card,
  CardMedia,
  CardContent,
  CardActions,
  IconButton,
  Button,
  Typography,
  Tooltip,
  Stack,
} from '@mui/material';
import { Favorite, FavoriteBorder, Edit, Delete, CalendarToday } from '@mui/icons-material';
import { useTheme } from '@mui/material/styles';
import { useUi } from '../Contexts/UiContext';
import styles from './VacationCard.module.css';

export function VacationCard({ 
  vacation, 
  isLiked, 
  likesCount, 
  isAdmin, 
  isAuthenticated, 
  onLikeToggle, 
  onEdit, 
  onDelete 
}) {
  const theme = useTheme();
  const { language, currency } = useUi();

  const formatDate = (value) => {
    try {
      const d = new Date(value);
      const dd = String(d.getDate()).padStart(2, '0');
      const mm = String(d.getMonth() + 1).padStart(2, '0');
      const yyyy = d.getFullYear();
      return `${dd}.${mm}.${yyyy}`;
    } catch {
      return value;
    }
  };

  const getImageSrc = (vacation) => {
    const name = (vacation?.vacation_file_name || '').trim();
    if (name && !/^https?:\/\//i.test(name)) {
      return `http://localhost:5000/uploads/${name}`;
    }
    return getCountryDefault(vacation?.country_name);
  };

  const getCountryDefault = (countryName) => {
    const countryDefaultMap = {
      israel: 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?q=80&w=1600&auto=format&fit=crop',
      greece: 'https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?q=80&w=1600&auto=format&fit=crop',
      italy: 'https://images.unsplash.com/photo-1515542622106-78bda8ba0e5b?q=80&w=1600&auto=format&fit=crop',
      rome: 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1600&auto=format&fit=crop',
      rhodes: 'https://images.unsplash.com/photo-1572252009286-268acec5ca0a?q=80&w=1600&auto=format&fit=crop',
      lahaina: 'https://images.unsplash.com/photo-1469796466635-455ede028aca?q=80&w=1600&auto=format&fit=crop',
      corfu: 'https://images.unsplash.com/photo-1628752068394-37be53ce38af?q=80&w=1600&auto=format&fit=crop',
      hilo: 'https://images.unsplash.com/photo-1505142468610-359e7d316be0?q=80&w=1600&auto=format&fit=crop',
      'montego bay': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?q=80&w=1600&auto=format&fit=crop',
      spain: 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?q=80&w=1600&auto=format&fit=crop',
      france: 'https://images.unsplash.com/photo-1502602898536-47ad22581b52?q=80&w=1600&auto=format&fit=crop',
      turkey: 'https://images.unsplash.com/photo-1541432901042-2d8bd64b4a9b?q=80&w=1600&auto=format&fit=crop',
      cyprus: 'https://images.unsplash.com/photo-1571501679680-de32f1e7aad4?q=80&w=1600&auto=format&fit=crop',
      'united kingdom': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?q=80&w=1600&auto=format&fit=crop',
      london: 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?q=80&w=1600&auto=format&fit=crop',
      paris: 'https://images.unsplash.com/photo-1502602898536-47ad22581b52?q=80&w=1600&auto=format&fit=crop',
      barcelona: 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?q=80&w=1600&auto=format&fit=crop',
      thailand: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1600&auto=format&fit=crop',
      japan: 'https://images.unsplash.com/photo-1480796927426-f609979314bd?q=80&w=1600&auto=format&fit=crop',
      switzerland: 'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?q=80&w=1600&auto=format&fit=crop',
      netherlands: 'https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?q=80&w=1600&auto=format&fit=crop',
      germany: 'https://images.unsplash.com/photo-1467269204594-9661b134dd2b?q=80&w=1600&auto=format&fit=crop',
      portugal: 'https://images.unsplash.com/photo-1555881400-74d7acaacd8b?q=80&w=1600&auto=format&fit=crop',
      dubai: 'https://images.unsplash.com/photo-1518684079-3c830dcef090?q=80&w=1600&auto=format&fit=crop',
      egypt: 'https://images.unsplash.com/photo-1539650116574-75c0c6d73f6e?q=80&w=1600&auto=format&fit=crop',
      morocco: 'https://images.unsplash.com/photo-1489749798305-4fea3ae436d0?q=80&w=1600&auto=format&fit=crop',
      bali: 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?q=80&w=1600&auto=format&fit=crop',
      maldives: 'https://images.unsplash.com/photo-1506084868230-bb9d95c24759?q=80&w=1600&auto=format&fit=crop',
      mexico: 'https://images.unsplash.com/photo-1518105779142-d975f22f1b0a?q=80&w=1600&auto=format&fit=crop',
      canada: 'https://images.unsplash.com/photo-1503614472-8c93d56e92ce?q=80&w=1600&auto=format&fit=crop',
      australia: 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?q=80&w=1600&auto=format&fit=crop',
      'new zealand': 'https://images.unsplash.com/photo-1469521669194-babb45599def?q=80&w=1600&auto=format&fit=crop',
      austria: 'https://images.unsplash.com/photo-1516550893923-42d28e5677af?q=80&w=1600&auto=format&fit=crop',
      norway: 'https://images.unsplash.com/photo-1523906834658-6e24ef2386f9?q=80&w=1600&auto=format&fit=crop',
      iceland: 'https://images.unsplash.com/photo-1539066033332-e2286ff4aa99?q=80&w=1600&auto=format&fit=crop',
      santorini: 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?q=80&w=1600&auto=format&fit=crop',
      prague: 'https://images.unsplash.com/photo-1541849546-216549ae216d?q=80&w=1600&auto=format&fit=crop',
      vienna: 'https://images.unsplash.com/photo-1516550893923-42d28e5677af?q=80&w=1600&auto=format&fit=crop',
      usa: 'https://images.unsplash.com/photo-1485738422979-f5c462d49f74?q=80&w=1600&auto=format&fit=crop',
      'united states': 'https://images.unsplash.com/photo-1485738422979-f5c462d49f74?q=80&w=1600&auto=format&fit=crop',
      'united states of america': 'https://images.unsplash.com/photo-1485738422979-f5c462d49f74?q=80&w=1600&auto=format&fit=crop',
      brazil: 'https://images.unsplash.com/photo-1483729558449-99ef09a8c325?q=80&w=1600&auto=format&fit=crop',
      'rio de janeiro': 'https://images.unsplash.com/photo-1483729558449-99ef09a8c325?q=80&w=1600&auto=format&fit=crop',
    };

    if (!countryName) return 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=60';
    
    const normalizeName = (str) => String(str || '')
      .toLowerCase()
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[^a-z\u0590-\u05FF\s]/g, '')
      .trim();

    const norm = normalizeName(countryName);
    return countryDefaultMap[norm] || 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=60';
  };

  const placeholderImg = 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&auto=format&fit=crop&q=60';
  const t = (he, en) => (language === 'he' ? he : en);
  const canLike = isAuthenticated && !isAdmin;
  const vacationId = Number(vacation.vacation_id);
  const start = vacation.vacation_start;
  const end = vacation.vacation_ends;

  return (
    <Box sx={{ display: 'flex' }}>
      <Card className={styles.vacationCard}>
        <Box className={styles.vacationImageContainer}>
          <CardMedia
            component="img"
            height="180"
            image={getImageSrc(vacation)}
            alt={vacation.vacation_description}
            onError={(e)=>{ e.currentTarget.src = placeholderImg; }}
            className={styles.vacationImage}
          />
          {/* gradient overlay */}
          <Box className={`${styles.imageOverlay} ${theme.palette.mode === 'light' ? styles.lightModeOverlay : ''}`} />
          {/* top overlays */}
          <Button
            aria-label={t('לייק', 'Like')}
            size="small"
            onClick={() => onLikeToggle(vacationId)}
            disabled={isAdmin || !isAuthenticated}
            className={`${styles.likeButton} ${theme.palette.mode === 'light' ? styles.lightModeLikeButton : ''}`}
          >
            {isLiked ? t('❤ Like', '❤ Like') : t('♡ Like', '♡ Like')} {likesCount ? likesCount : ''}
          </Button>
          {isAdmin && (
            <Stack direction="row" spacing={1} className={styles.adminActions}>
              <Button aria-label={t('עריכה', 'Edit')} size="small" variant="outlined" color="inherit" onClick={() => onEdit(vacationId)} startIcon={<Edit />} className={styles.adminButton}>Edit</Button>
              <Button aria-label={t('מחיקה', 'Delete')} size="small" variant="outlined" color="inherit" onClick={() => onDelete(vacationId)} startIcon={<Delete />} className={styles.adminButton}>Delete</Button>
            </Stack>
          )}
          {/* title overlay */}
          <Typography variant="h5" className={styles.vacationTitle}>
            {vacation.country_name}
          </Typography>
        </Box>

        {/* date bar */}
        <Box className={`${styles.dateBar} ${theme.palette.mode === 'light' ? styles.lightModeDateBar : ''}`}>
          <CalendarToday fontSize="small" />
          <Typography variant="body1" className={styles.dateText}>{`${formatDate(start)} - ${formatDate(end)}`}</Typography>
        </Box>

        <CardContent className={styles.vacationContent}>
          <Typography variant="body2" className={styles.vacationDescription}>
            {vacation.vacation_description}
          </Typography>
          <Button aria-label={t('מחיר חופשה', 'Vacation price')} variant="contained" fullWidth className={styles.priceButton}>
            {currency === 'ILS' ? '₪' : currency === 'EUR' ? '€' : '$'}
            {Number(vacation.vacation_price).toLocaleString(language === 'he' ? 'he-IL' : 'en-US')}
          </Button>
        </CardContent>

        {!isAdmin && (
          <CardActions className={styles.vacationActions}>
            <Tooltip title={canLike ? (isLiked ? t('בטל לייק', 'Unlike') : t('לייק', 'Like')) : t('יש להתחבר כדי ללייק', 'Login to like')}>
              <span>
                <IconButton
                  color={isLiked ? 'error' : 'default'}
                  onClick={() => onLikeToggle(vacationId)}
                  disabled={!canLike}
                  aria-label="like"
                >
                  {isLiked ? <Favorite /> : <FavoriteBorder />}
                </IconButton>
              </span>
            </Tooltip>
            <Typography variant="caption" className={styles.likesCount}>
              {likesCount} {t('לייקים', 'likes')}
            </Typography>
          </CardActions>
        )}
      </Card>
    </Box>
  );
}
