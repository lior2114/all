import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Paper, 
  Avatar,
  Button,
  Divider,
  Grid,
  Card,
  CardContent,
  CardMedia,
  Chip,
  CircularProgress,
  Alert,
  TextField,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  IconButton
} from '@mui/material';
import { Edit, Save, Cancel, PhotoCamera } from '@mui/icons-material';
import { useUser } from '../Contexts/UserContext';
import { useVacations } from '../Contexts/VacationsContext';
import { useLikes } from '../Contexts/LikesContext';
import { useNavigate } from 'react-router-dom';
import { getUserFavoriteVacations, updateUser, updateProfileImage, removeProfileImage as removeProfileImageAPI } from '../api/api';

const Profile = () => {
  const { user, logout, updateUser: updateUserContext } = useUser();
  const { formatDate, formatPrice, calculateDuration, getVacationImage } = useVacations();
  const { likes } = useLikes();
  const navigate = useNavigate();
  const [favoriteVacations, setFavoriteVacations] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  // State לעריכת פרטים
  const [editMode, setEditMode] = useState(false);
  const [editDialogOpen, setEditDialogOpen] = useState(false);
  const [editForm, setEditForm] = useState({
    first_name: '',
    last_name: '',
    user_email: '',
    password: ''
  });
  const [editLoading, setEditLoading] = useState(false);
  const [editError, setEditError] = useState('');
  
  // State לתמונת פרופיל
  const [profileImage, setProfileImage] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [imageLoading, setImageLoading] = useState(false);
  const [imageError, setImageError] = useState('');

  useEffect(() => {
    if (user && user.user_id) {
      fetchFavoriteVacations();
    }
  }, [user, likes]);

  useEffect(() => {
    if (user) {
      setEditForm({
        first_name: user.first_name || '',
        last_name: user.last_name || '',
        user_email: user.user_email || '',
        password: ''
      });
    }
  }, [user]);

  const fetchFavoriteVacations = async () => {
    if (!user || !user.user_id) return;
    
    try {
      setLoading(true);
      setError('');
      const favoriteVacationsData = await getUserFavoriteVacations(user.user_id);
      setFavoriteVacations(favoriteVacationsData);
    } catch (err) {
      console.error('Error fetching favorite vacations:', err);
      setError('שגיאה בטעינת החופשות האהובות');
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  const handleEditClick = () => {
    setEditDialogOpen(true);
  };

  const handleEditClose = () => {
    setEditDialogOpen(false);
    setEditError('');
  };

  const handleEditSubmit = async () => {
    if (!user || !user.user_id) return;

    try {
      setEditLoading(true);
      setEditError('');
      
      const updateData = {
        first_name: editForm.first_name,
        last_name: editForm.last_name,
        user_email: editForm.user_email
      };
      
      if (editForm.password) {
        updateData.password = editForm.password;
      }
      
      const result = await updateUser(user.user_id, updateData);
      
      // עדכון הקונטקסט
      updateUserContext({
        ...user,
        ...updateData
      });
      
      setEditDialogOpen(false);
      setEditForm({ ...editForm, password: '' });
    } catch (err) {
      setEditError(err.message || 'שגיאה בעדכון הפרטים');
    } finally {
      setEditLoading(false);
    }
  };

  // פונקציות לתמונת פרופיל
  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      // בדיקת סוג הקובץ
      if (!file.type.startsWith('image/')) {
        setImageError('אנא בחר קובץ תמונה בלבד');
        return;
      }
      
      // בדיקת גודל הקובץ (מקסימום 5MB)
      if (file.size > 5 * 1024 * 1024) {
        setImageError('גודל הקובץ חייב להיות פחות מ-5MB');
        return;
      }
      
      setProfileImage(file);
      setImageError('');
      
      // יצירת תצוגה מקדימה
      const reader = new FileReader();
      reader.onload = (e) => {
        setImagePreview(e.target.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleImageUpload = async () => {
    if (!profileImage || !user || !user.user_id) return;

    try {
      setImageLoading(true);
      setImageError('');
      
      const formData = new FormData();
      formData.append('profile_image', profileImage);
      
      // קריאה לשרת לעדכון תמונת הפרופיל
      const result = await updateProfileImage(user.user_id, formData);
      
      // עדכון הקונטקסט עם התמונה החדשה
      updateUserContext({
        ...user,
        profile_image: result.profile_image_url ? `http://localhost:5000${result.profile_image_url}` : null
      });
      
      // איפוס המצב
      setProfileImage(null);
      setImagePreview(null);
      
    } catch (err) {
      setImageError(err.message || 'שגיאה בעדכון תמונת הפרופיל');
    } finally {
      setImageLoading(false);
    }
  };

  const removeProfileImage = async () => {
    if (!user || !user.user_id) return;

    try {
      setImageLoading(true);
      setImageError('');
      
      // קריאה לשרת להסרת תמונת הפרופיל
      await removeProfileImageAPI(user.user_id);
      
      // עדכון הקונטקסט - הסרת תמונת הפרופיל
      updateUserContext({
        ...user,
        profile_image: null
      });
      
      // איפוס המצב
      setProfileImage(null);
      setImagePreview(null);
      
    } catch (err) {
      setImageError(err.message || 'שגיאה בהסרת תמונת הפרופיל');
    } finally {
      setImageLoading(false);
    }
  };

  if (!user) {
    return (
      <Container maxWidth="sm" sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center',
        minHeight: '80vh',
        justifyContent: 'center'
      }}>
        <Typography variant="h5" color="text.secondary">
          אנא התחבר כדי לצפות בפרופיל שלך
        </Typography>
      </Container>
    );
  }

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
          הפרופיל שלי
        </Typography>
        
        <Paper 
          elevation={3} 
          sx={{ 
            p: 4, 
            borderRadius: 3,
            backgroundColor: 'background.paper',
            mb: 4
          }}
        >
                     <Box sx={{ 
             display: 'flex', 
             flexDirection: 'column', 
             alignItems: 'center', 
             mb: 4,
             p: 4,
             borderRadius: 3,
             backgroundColor: 'primary.light',
             background: 'linear-gradient(135deg, #1976d2 0%, #42a5f5 100%)',
             color: 'white',
             boxShadow: 3
           }}>
             <Box sx={{ position: 'relative', mb: 3 }}>
               <Avatar 
                 sx={{ 
                   width: 120, 
                   height: 120, 
                   bgcolor: 'white',
                   color: 'primary.main',
                   fontSize: '3rem',
                   border: '4px solid white',
                   boxShadow: 3,
                   backgroundImage: user.profile_image ? `url(${user.profile_image})` : 'none',
                   backgroundSize: 'cover',
                   backgroundPosition: 'center'
                 }}
               >
                 {!user.profile_image && (user.first_name?.charAt(0) || user.user_email?.charAt(0) || 'U')}
               </Avatar>
               
               {/* כפתור עדכון תמונה */}
               <IconButton
                 sx={{
                   position: 'absolute',
                   bottom: 0,
                   right: 0,
                   bgcolor: 'primary.main',
                   color: 'white',
                   border: '2px solid white',
                   '&:hover': {
                     bgcolor: 'primary.dark',
                     transform: 'scale(1.1)'
                   },
                   transition: 'all 0.2s ease-in-out'
                 }}
                 onClick={() => document.getElementById('profile-image-input').click()}
               >
                 <PhotoCamera />
               </IconButton>
               
               <input
                 id="profile-image-input"
                 type="file"
                 accept="image/*"
                 style={{ display: 'none' }}
                 onChange={handleImageChange}
               />
             </Box>
             
             <Typography 
               variant="h3" 
               component="h2" 
               gutterBottom
               sx={{ 
                 fontWeight: 'bold',
                 textAlign: 'center',
                 textShadow: '0 2px 4px rgba(0,0,0,0.3)'
               }}
             >
               {user.first_name && user.last_name 
                 ? `${user.first_name} ${user.last_name}`
                 : user.user_email
               }
             </Typography>
             
             <Typography 
               variant="h6" 
               sx={{ 
                 opacity: 0.9,
                 textAlign: 'center'
               }}
             >
               ברוך הבא לפרופיל שלך
             </Typography>
           </Box>
          
                     <Divider sx={{ my: 3 }} />
           
           {/* אזור תמונת פרופיל */}
           {(profileImage || imagePreview || imageError) && (
             <Box sx={{ 
               mb: 3, 
               p: 3, 
               borderRadius: 2, 
               backgroundColor: 'grey.50',
               border: '1px solid',
               borderColor: 'grey.200'
             }}>
               <Typography variant="h6" sx={{ mb: 2, textAlign: 'center', fontWeight: 'bold' }}>
                 עדכון תמונת פרופיל
               </Typography>
               
               {imageError && (
                 <Alert severity="error" sx={{ mb: 2 }}>
                   {imageError}
                 </Alert>
               )}
               
               {imagePreview && (
                 <Box sx={{ textAlign: 'center', mb: 2 }}>
                   <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                     תצוגה מקדימה:
                   </Typography>
                   <Avatar 
                     sx={{ 
                       width: 80, 
                       height: 80, 
                       mx: 'auto',
                       backgroundImage: `url(${imagePreview})`,
                       backgroundSize: 'cover',
                       backgroundPosition: 'center'
                     }}
                   />
                 </Box>
               )}
               
               <Box sx={{ display: 'flex', justifyContent: 'center', gap: 2, flexWrap: 'wrap' }}>
                 {profileImage && (
                   <Button
                     variant="contained"
                     color="primary"
                     onClick={handleImageUpload}
                     disabled={imageLoading}
                     startIcon={imageLoading ? <CircularProgress size={20} /> : <Save />}
                     sx={{ 
                       minWidth: 120,
                       background: 'linear-gradient(45deg, #1976d2 30%, #42a5f5 90%)',
                       '&:hover': {
                         background: 'linear-gradient(45deg, #1565c0 30%, #1976d2 90%)'
                       }
                     }}
                   >
                     {imageLoading ? 'שומר...' : 'שמור תמונה'}
                   </Button>
                 )}
                 
                 <Button
                   variant="outlined"
                   color="secondary"
                   onClick={() => {
                     setProfileImage(null);
                     setImagePreview(null);
                     setImageError('');
                   }}
                   sx={{ minWidth: 120 }}
                 >
                   ביטול
                 </Button>
                 
                 {user.profile_image && (
                   <Button
                     variant="outlined"
                     color="error"
                     onClick={removeProfileImage}
                     sx={{ minWidth: 120 }}
                   >
                     הסר תמונה
                   </Button>
                 )}
               </Box>
             </Box>
           )}
           
           <Box sx={{  
             display: 'flex', 
             flexDirection: { xs: 'column', md: 'row' }, 
             gap: 3,
             justifyContent: 'center',
             alignItems: 'stretch',
             mt: 3,
             maxWidth: 600,
             mx: 'auto'
           }}>
             {user.first_name && (
               <Box sx={{ 
                 flex: { xs: 'none', md: 1 },
                 maxWidth: { xs: '100%', md: 180 },
                 textAlign: 'center',
                 p: 3,
                 borderRadius: 2,
                 backgroundColor: 'grey.50',
                 border: '1px solid',
                 borderColor: 'grey.200',
                 minHeight: 120,
                 display: 'flex',
                 flexDirection: 'column',
                 justifyContent: 'center',
                 transition: 'all 0.3s ease',
                 '&:hover': {
                   transform: 'translateY(-2px)',
                   boxShadow: 3,
                   backgroundColor: 'grey.100'
                 }
               }}>
                 <Typography variant="h6" color="text.secondary" sx={{ mb: 1, fontWeight: 'bold' }}>
                   שם פרטי
                 </Typography>
                 <Typography variant="h5" sx={{ fontWeight: 'bold', color: 'primary.main' }}>
                   {user.first_name}
                 </Typography>
               </Box>
             )}
             
             {user.last_name && (
               <Box sx={{ 
                 flex: { xs: 'none', md: 1 },
                 maxWidth: { xs: '100%', md: 180 },
                 textAlign: 'center',
                 p: 3,
                 borderRadius: 2,
                 backgroundColor: 'grey.50',
                 border: '1px solid',
                 borderColor: 'grey.200',
                 minHeight: 120,
                 display: 'flex',
                 flexDirection: 'column',
                 justifyContent: 'center',
                 transition: 'all 0.3s ease',
                 '&:hover': {
                   transform: 'translateY(-2px)',
                   boxShadow: 3,
                   backgroundColor: 'grey.100'
                 }
               }}>
                 <Typography variant="h6" color="text.secondary" sx={{ mb: 1, fontWeight: 'bold' }}>
                   שם משפחה
                 </Typography>
                 <Typography variant="h5" sx={{ fontWeight: 'bold', color: 'primary.main' }}>
                   {user.last_name}
                 </Typography>
               </Box>
             )}
             
             <Box sx={{ 
               flex: { xs: 'none', md: 1 },
               minWidth: { xs: '100%', md: 280 },
               maxWidth: { xs: '100%', md: 'none' },
               textAlign: 'center',
               p: 3,
               borderRadius: 2,
               backgroundColor: 'grey.50',
               border: '1px solid',
               borderColor: 'grey.200',
               minHeight: 120,
               display: 'flex',
               flexDirection: 'column',
               justifyContent: 'center',
               transition: 'all 0.3s ease',
               '&:hover': {
                 transform: 'translateY(-2px)',
                 boxShadow: 3,
                 backgroundColor: 'grey.100'
               }
             }}>
               <Typography variant="h6" color="text.secondary" sx={{ mb: 1, fontWeight: 'bold' }}>
                 אימייל
               </Typography>
               <Typography 
                 variant="h5" 
                 sx={{ 
                   fontWeight: 'bold', 
                   color: 'primary.main',
                   fontSize: { xs: '1.2rem', md: '1.3rem' },
                   wordBreak: 'break-all',
                   lineHeight: 1.2
                 }}
               >
                 {user.user_email}
               </Typography>
             </Box>
           </Box>
          
                     <Box sx={{ 
             mt: 4, 
             display: 'flex', 
             justifyContent: 'center', 
             gap: 3,
             flexWrap: 'wrap'
           }}>
             <Button 
               variant="outlined" 
               onClick={() => navigate('/')}
               sx={{ 
                 minWidth: 140,
                 py: 1.5,
                 px: 3,
                 borderRadius: 2,
                 fontWeight: 'bold',
                 borderWidth: 2,
                 '&:hover': {
                   borderWidth: 2,
                   transform: 'translateY(-2px)',
                   boxShadow: 3
                 },
                 transition: 'all 0.2s ease-in-out'
               }}
             >
               חזרה לדף הבית
             </Button>
             <Button 
               variant="contained" 
               color="primary"
               startIcon={<Edit />}
               onClick={handleEditClick}
               sx={{ 
                 minWidth: 140,
                 py: 1.5,
                 px: 3,
                 borderRadius: 2,
                 fontWeight: 'bold',
                 background: 'linear-gradient(45deg, #1976d2 30%, #42a5f5 90%)',
                 boxShadow: '0 3px 5px 2px rgba(25, 118, 210, .3)',
                 '&:hover': {
                   background: 'linear-gradient(45deg, #1565c0 30%, #1976d2 90%)',
                   transform: 'translateY(-2px)',
                   boxShadow: '0 5px 8px 2px rgba(25, 118, 210, .4)'
                 },
                 transition: 'all 0.2s ease-in-out'
               }}
             >
               ערוך פרטים
             </Button>
             <Button 
               variant="contained" 
               color="error"
               onClick={handleLogout}
               sx={{ 
                 minWidth: 140,
                 py: 1.5,
                 px: 3,
                 borderRadius: 2,
                 fontWeight: 'bold',
                 background: 'linear-gradient(45deg, #d32f2f 30%, #f44336 90%)',
                 boxShadow: '0 3px 5px 2px rgba(211, 47, 47, .3)',
                 '&:hover': {
                   background: 'linear-gradient(45deg, #c62828 30%, #d32f2f 90%)',
                   transform: 'translateY(-2px)',
                   boxShadow: '0 5px 8px 2px rgba(211, 47, 47, .4)'
                 },
                 transition: 'all 0.2s ease-in-out'
               }}
             >
               התנתק
             </Button>
           </Box>
        </Paper>

        {/* החופשות האהובות */}
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
              fontWeight: 'bold',
              color: 'primary.main',
              textAlign: 'center'
            }}
          >
            החופשות האהובות שלי ❤️
          </Typography>

          {loading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 4 }}>
              <CircularProgress />
            </Box>
          )}

          {error && (
            <Alert severity="error" sx={{ mb: 3 }}>
              {error}
            </Alert>
          )}

          {!loading && !error && favoriteVacations.length === 0 && (
            <Box sx={{ textAlign: 'center', py: 4 }}>
              <Typography variant="h6" color="text.secondary" sx={{ mb: 2 }}>
                עדיין אין לך חופשות אהובות
              </Typography>
              <Typography variant="body1" color="text.secondary" sx={{ mb: 3 }}>
                לך לדף החופשות ועשה לייק לחופשות שאתה אוהב!
              </Typography>
              <Button 
                variant="contained" 
                color="primary"
                onClick={() => navigate('/vacations')}
              >
                לך לחופשות
              </Button>
            </Box>
          )}

          {!loading && !error && favoriteVacations.length > 0 && (
            <Grid container spacing={3}>
              {favoriteVacations.map((vacation) => (
                <Grid size={{ xs: 12, sm: 6, md: 4 }} key={`favorite-${vacation.vacation_id}`}>
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
                      height="150"
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
                      
                      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <Typography variant="body2" color="text.secondary">
                          מ: {formatDate(vacation.vacation_start)}
                        </Typography>
                        <Typography variant="body2" color="text.secondary">
                          עד: {formatDate(vacation.vacation_ends)}
                        </Typography>
                      </Box>
                      
                      <Box sx={{ mt: 2, textAlign: 'center' }}>
                        <Button 
                          variant="outlined" 
                          color="primary"
                          fullWidth
                          size="small"
                          onClick={() => navigate('/vacations')}
                          sx={{ borderRadius: 2 }}
                        >
                          צפה בחופשה
                        </Button>
                      </Box>
                    </CardContent>
                  </Card>
                </Grid>
              ))}
            </Grid>
          )}
        </Paper>
      </Box>

      {/* דיאלוג עריכת פרטים */}
      <Dialog open={editDialogOpen} onClose={handleEditClose} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ textAlign: 'center', fontWeight: 'bold' }}>
          עריכת פרטים
        </DialogTitle>
        <DialogContent>
          <Box sx={{ pt: 2 }}>
            {editError && (
              <Alert severity="error" sx={{ mb: 2 }}>
                {editError}
              </Alert>
            )}
            
            <Grid container spacing={2}>
              <Grid size={{ xs: 12, sm: 6 }}>
                <TextField
                  fullWidth
                  label="שם פרטי"
                  value={editForm.first_name}
                  onChange={(e) => setEditForm({ ...editForm, first_name: e.target.value })}
                  variant="outlined"
                  sx={{ mb: 2 }}
                />
              </Grid>
              <Grid size={{ xs: 12, sm: 6 }}>
                <TextField
                  fullWidth
                  label="שם משפחה"
                  value={editForm.last_name}
                  onChange={(e) => setEditForm({ ...editForm, last_name: e.target.value })}
                  variant="outlined"
                  sx={{ mb: 2 }}
                />
              </Grid>
              <Grid size={{ xs: 12 }}>
                <TextField
                  fullWidth
                  label="אימייל"
                  type="email"
                  value={editForm.user_email}
                  onChange={(e) => setEditForm({ ...editForm, user_email: e.target.value })}
                  variant="outlined"
                  sx={{ mb: 2 }}
                />
              </Grid>
              <Grid size={{ xs: 12 }}>
                <TextField
                  fullWidth
                  label="סיסמה חדשה (אופציונלי)"
                  type="password"
                  value={editForm.password}
                  onChange={(e) => setEditForm({ ...editForm, password: e.target.value })}
                  variant="outlined"
                  helperText="השאר ריק אם אינך רוצה לשנות את הסיסמה"
                />
              </Grid>
            </Grid>
          </Box>
        </DialogContent>
        <DialogActions sx={{ p: 3 }}>
          <Button 
            onClick={handleEditClose} 
            color="inherit"
            startIcon={<Cancel />}
          >
            ביטול
          </Button>
          <Button 
            onClick={handleEditSubmit} 
            variant="contained" 
            color="primary"
            disabled={editLoading}
            startIcon={editLoading ? <CircularProgress size={20} /> : <Save />}
          >
            {editLoading ? 'שומר...' : 'שמור שינויים'}
          </Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default Profile;
