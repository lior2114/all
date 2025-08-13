import React from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Paper, 
  Grid, 
  Card, 
  CardContent,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  CircularProgress,
  Alert
} from '@mui/material';
import { useVacations } from '../Contexts/VacationsContext';
import { useLikes } from '../Contexts/LikesContext';
import { useUser } from '../Contexts/UserContext';

const Statistics = () => {
  const { vacations, loading: vacationsLoading, error: vacationsError, formatPrice } = useVacations();
  const { likes, loading: likesLoading, error: likesError, isLikedByUser } = useLikes();
  const { user } = useUser();

  const loading = vacationsLoading || likesLoading;
  const error = vacationsError || likesError;

  // חישוב סטטיסטיקות
  const totalVacations = vacations.length;
  const totalLikes = likes.length;
  const averagePrice = vacations.length > 0 
    ? vacations.reduce((sum, vacation) => sum + vacation.vacation_price, 0) / vacations.length 
    : 0;

  // החופשה הכי אהובה
  const getMostLikedVacation = () => {
    if (vacations.length === 0) return null;
    
    const vacationLikes = vacations.map(vacation => ({
      vacation,
      likes: likes.filter(like => like[1] === vacation.vacation_id).length
    }));
    
    return vacationLikes.reduce((max, current) => 
      current.likes > max.likes ? current : max
    );
  };

  const mostLikedVacation = getMostLikedVacation();

  // החופשות שהמשתמש הנוכחי עשה להן לייק
  const getUserLikedVacations = () => {
    if (!user || !user.user_id) return [];
    
    const userLikes = likes.filter(like => like[0] === user.user_id);
    return vacations.filter(vacation => 
      userLikes.some(like => like[1] === vacation.vacation_id)
    );
  };

  const userLikedVacations = getUserLikedVacations();

  // בדיקה - הדפסה לקונסול
  console.log('Statistics Data:', {
    totalVacations,
    totalLikes,
    averagePrice,
    mostLikedVacation,
    userLikedVacations: userLikedVacations.length,
    vacations: vacations.length,
    likes: likes.length
  });

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
            טוען סטטיסטיקות...
          </Typography>
        </Box>
      </Container>
    );
  }

  if (error) {
    return (
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Alert severity="error" sx={{ mb: 3 }}>
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
          סטטיסטיקות
        </Typography>
        <Typography 
          variant="h5" 
          color="text.secondary"
          sx={{ mb: 3 }}
        >
          סקירה כללית של החופשות והלייקים
        </Typography>
      </Box>

      {/* כרטיסי סטטיסטיקות */}
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ textAlign: 'center', p: 2 }}>
            <CardContent>
              <Typography variant="h4" color="primary.main" sx={{ fontWeight: 'bold' }}>
                {totalVacations}
              </Typography>
              <Typography variant="h6" color="text.secondary">
                חופשות
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ textAlign: 'center', p: 2 }}>
            <CardContent>
              <Typography variant="h4" color="secondary.main" sx={{ fontWeight: 'bold' }}>
                {totalLikes}
              </Typography>
              <Typography variant="h6" color="text.secondary">
                לייקים
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ textAlign: 'center', p: 2 }}>
            <CardContent>
              <Typography variant="h4" color="success.main" sx={{ fontWeight: 'bold' }}>
                {formatPrice(averagePrice)}
              </Typography>
              <Typography variant="h6" color="text.secondary">
                מחיר ממוצע
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ textAlign: 'center', p: 2 }}>
            <CardContent>
              <Typography variant="h4" color="warning.main" sx={{ fontWeight: 'bold' }}>
                {userLikedVacations.length}
              </Typography>
              <Typography variant="h6" color="text.secondary">
                לייקים שלך
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* החופשה הכי אהובה */}
      {mostLikedVacation && (
        <Paper sx={{ p: 3, mb: 4 }}>
          <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold', mb: 2 }}>
            החופשה הכי אהובה ❤️
          </Typography>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
            <Chip 
              label={`${mostLikedVacation.likes} לייקים`} 
              color="primary" 
              size="large"
            />
            <Typography variant="h6">
              {mostLikedVacation.vacation.country_name} - {formatPrice(mostLikedVacation.vacation.vacation_price)}
            </Typography>
          </Box>
        </Paper>
      )}

      {/* טבלת כל החופשות עם לייקים */}
      <Paper sx={{ p: 3, mb: 4 }}>
        <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold', mb: 3 }}>
          כל החופשות עם מספר לייקים
        </Typography>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontWeight: 'bold' }}>יעד</TableCell>
                <TableCell sx={{ fontWeight: 'bold' }}>תיאור</TableCell>
                <TableCell sx={{ fontWeight: 'bold' }}>מחיר</TableCell>
                <TableCell sx={{ fontWeight: 'bold' }}>לייקים</TableCell>
                <TableCell sx={{ fontWeight: 'bold' }}>לייק שלך</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {vacations.map((vacation) => {
                const likesCount = likes.filter(like => like[1] === vacation.vacation_id).length;
                const isLiked = user && isLikedByUser(vacation.vacation_id);
                
                return (
                  <TableRow key={`vacation-${vacation.vacation_id}`}>
                    <TableCell>{vacation.country_name}</TableCell>
                    <TableCell>{vacation.vacation_description}</TableCell>
                    <TableCell>{formatPrice(vacation.vacation_price)}</TableCell>
                    <TableCell>
                      <Chip label={likesCount} color="primary" size="small" />
                    </TableCell>
                    <TableCell>
                      {isLiked ? (
                        <Chip label="כן" color="success" size="small" />
                      ) : (
                        <Chip label="לא" color="default" size="small" />
                      )}
                    </TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>

      {/* החופשות שהמשתמש עשה להן לייק */}
      {user && userLikedVacations.length > 0 && (
        <Paper sx={{ p: 3 }}>
          <Typography variant="h5" gutterBottom sx={{ fontWeight: 'bold', mb: 3 }}>
            החופשות שאתה אוהב ❤️
          </Typography>
          <Grid container spacing={2}>
            {userLikedVacations.map((vacation) => (
              <Grid size={{ xs: 12, sm: 6, md: 4 }} key={`user-liked-${vacation.vacation_id}`}>
                <Card sx={{ p: 2 }}>
                  <CardContent>
                    <Typography variant="h6" sx={{ fontWeight: 'bold', mb: 1 }}>
                      {vacation.country_name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                      {vacation.vacation_description}
                    </Typography>
                    <Typography variant="body1" color="primary.main" sx={{ fontWeight: 'bold' }}>
                      {formatPrice(vacation.vacation_price)}
                    </Typography>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Paper>
      )}
    </Container>
  );
};

export default Statistics;
