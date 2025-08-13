import React, { useState, useMemo } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Paper, 
  Grid, 
  Card, 
  CardContent, 
  CardMedia,
  Chip,
  Rating,
  CircularProgress,
  Alert,
  Button,
  IconButton,
  Badge,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Slider
} from '@mui/material';
import { Favorite, FavoriteBorder, Search } from '@mui/icons-material';
import { useVacations } from '../Contexts/VacationsContext';
import { useLikes } from '../Contexts/LikesContext';
import { useUser } from '../Contexts/UserContext';

const Vacations = () => {
  const { 
    vacations, 
    loading, 
    error, 
    fetchVacations,
    formatDate, 
    formatPrice, 
    calculateDuration,
    getVacationImage 
  } = useVacations();
  
  const { 
    toggleLike, 
    isLikedByUser, 
    getLikesCount 
  } = useLikes();
  
  const { isAuthenticated } = useUser();

  // State לחיפוש
  const [searchTerm, setSearchTerm] = useState('');
  const [priceRange, setPriceRange] = useState([0, 10000]);
  const [durationFilter, setDurationFilter] = useState('all');

  // פילטור החופשות
  const filteredVacations = useMemo(() => {
    return vacations.filter(vacation => {
      // חיפוש טקסט
      const matchesSearch = vacation.country_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
                           vacation.vacation_description.toLowerCase().includes(searchTerm.toLowerCase());
      
      // פילטר מחיר
      const matchesPrice = vacation.vacation_price >= priceRange[0] && vacation.vacation_price <= priceRange[1];
      
      // פילטר משך
      const duration = calculateDuration(vacation.vacation_start, vacation.vacation_ends);
      let matchesDuration = true;
      if (durationFilter === 'short') matchesDuration = duration <= 7;
      else if (durationFilter === 'medium') matchesDuration = duration > 7 && duration <= 14;
      else if (durationFilter === 'long') matchesDuration = duration > 14;
      
      return matchesSearch && matchesPrice && matchesDuration;
    });
  }, [vacations, searchTerm, priceRange, durationFilter]);

  // טיפול בלייק/אנלייק
  const handleLikeToggle = async (vacationId) => {
    if (!isAuthenticated) {
      alert('אנא התחבר כדי לעשות לייק');
      return;
    }

    try {
      await toggleLike(vacationId);
    } catch (err) {
      alert('שגיאה בעדכון הלייק: ' + err.message);
    }
  };

  if (loading) {
    return (
      <Container maxWidth="lg" sx={{ 
        display: 'flex', 
        justifyContent: 'center', 
        alignItems: 'center',
        minHeight: '60vh'
      }}>
        <Box sx={{ textAlign: 'center' }}>
          <CircularProgress size={60} sx={{ mb: 2 }} />
          <Typography variant="h6" color="text.secondary">
            טוען חופשות...
          </Typography>
        </Box>
      </Container>
    );
  }

  if (error) {
    return (
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Alert 
          severity="error" 
          sx={{ mb: 3 }}
          action={
            <Button color="inherit" size="small" onClick={fetchVacations}>
              נסה שוב
            </Button>
          }
        >
          {error}
        </Alert>
      </Container>
    );
  }

  return (
    <Container maxWidth="lg" sx={{ py: 4 }}>
      <Box sx={{ textAlign: 'center', mb: 4 }}>
        <Typography 
          variant="h2" 
          component="h1" 
          gutterBottom
          sx={{ 
            fontWeight: 'bold',
            color: 'primary.main',
            mb: 2
          }}
        >
          חופשות מדהימות
        </Typography>
        <Typography 
          variant="h5" 
          color="text.secondary"
          sx={{ mb: 3 }}
        >
          גלה יעדים מרהיבים וחופשות בלתי נשכחות
        </Typography>
      </Box>

      {/* מנוע חיפוש */}
      <Paper sx={{ p: 3, mb: 4 }}>
        <Typography variant="h6" gutterBottom sx={{ fontWeight: 'bold', mb: 3 }}>
          <Search sx={{ mr: 1, verticalAlign: 'middle' }} />
          חיפוש חופשות
        </Typography>
        
        <Grid container spacing={3}>
          <Grid size={{ xs: 12, md: 4 }}>
            <TextField
              fullWidth
              label="חיפוש לפי יעד או תיאור"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              variant="outlined"
            />
          </Grid>
          
          <Grid size={{ xs: 12, md: 4 }}>
            <FormControl fullWidth>
              <InputLabel>משך החופשה</InputLabel>
              <Select
                value={durationFilter}
                label="משך החופשה"
                onChange={(e) => setDurationFilter(e.target.value)}
              >
                <MenuItem value="all">כל החופשות</MenuItem>
                <MenuItem value="short">עד שבוע</MenuItem>
                <MenuItem value="medium">שבוע-שבועיים</MenuItem>
                <MenuItem value="long">מעל שבועיים</MenuItem>
              </Select>
            </FormControl>
          </Grid>
          
          <Grid size={{ xs: 12, md: 4 }}>
            <Box>
              <Typography gutterBottom>
                טווח מחירים: {formatPrice(priceRange[0])} - {formatPrice(priceRange[1])}
              </Typography>
              <Slider
                value={priceRange}
                onChange={(e, newValue) => setPriceRange(newValue)}
                valueLabelDisplay="auto"
                min={0}
                max={10000}
                step={100}
              />
            </Box>
          </Grid>
        </Grid>
        
        <Box sx={{ mt: 2, textAlign: 'center' }}>
          <Typography variant="body2" color="text.secondary">
            נמצאו {filteredVacations.length} חופשות מתוך {vacations.length}
          </Typography>
        </Box>
      </Paper>

      {!filteredVacations || filteredVacations.length === 0 ? (
        <Paper sx={{ p: 4, textAlign: 'center' }}>
          <Typography variant="h6" color="text.secondary">
            לא נמצאו חופשות
          </Typography>
        </Paper>
      ) : (
        <Grid container spacing={3}>
          {filteredVacations.map((vacation) => (
            <Grid size={{ xs: 12, sm: 6, md: 4 }} key={`vacation-${vacation.vacation_id}`}>
              <Card 
                sx={{ 
                  height: '100%',
                  display: 'flex',
                  flexDirection: 'column',
                  transition: 'transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out',
                  '&:hover': {
                    transform: 'translateY(-4px)',
                    boxShadow: 4
                  }
                }}
              >
                <CardMedia
                  component="img"
                  height="200"
                  image={getVacationImage(vacation.country_name)}
                  alt={vacation.country_name || 'Vacation'}
                  sx={{ objectFit: 'cover' }}
                />
                <CardContent sx={{ flexGrow: 1, textAlign: 'right' }}>
                  <Typography 
                    variant="h6" 
                    component="h3" 
                    gutterBottom
                    sx={{ fontWeight: 'bold' }}
                  >
                    {vacation.country_name}
                  </Typography>
                  
                  <Typography 
                    variant="body2" 
                    color="text.secondary" 
                    sx={{ mb: 2, minHeight: '3em' }}
                  >
                    {vacation.vacation_description}
                  </Typography>
                  
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                    <Typography variant="h6" color="primary.main" sx={{ fontWeight: 'bold' }}>
                      {formatPrice(vacation.vacation_price)}
                    </Typography>
                    <Chip 
                      label={`${calculateDuration(vacation.vacation_start, vacation.vacation_ends)} ימים`} 
                      color="secondary" 
                      size="small"
                    />
                  </Box>
                  
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
                    <Typography variant="body2" color="text.secondary">
                      מ: {formatDate(vacation.vacation_start)}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      עד: {formatDate(vacation.vacation_ends)}
                    </Typography>
                  </Box>
                  
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <Button 
                      variant="contained" 
                      color="primary"
                      disabled={!isAuthenticated}
                      sx={{ borderRadius: 2 }}
                    >
                      הזמן עכשיו
                    </Button>
                    
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                      <IconButton 
                        onClick={() => handleLikeToggle(vacation.vacation_id)}
                        color="primary"
                        sx={{ 
                          '&:hover': { 
                            transform: 'scale(1.1)' 
                          } 
                        }}
                      >
                        {isLikedByUser(vacation.vacation_id) ? (
                          <Favorite sx={{ color: 'red' }} />
                        ) : (
                          <FavoriteBorder />
                        )}
                      </IconButton>
                      <Badge badgeContent={getLikesCount(vacation.vacation_id)} color="primary">
                        <Typography variant="body2" color="text.secondary">
                          לייקים
                        </Typography>
                      </Badge>
                    </Box>
                  </Box>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      )}
    </Container>
  );
};

export default Vacations;
