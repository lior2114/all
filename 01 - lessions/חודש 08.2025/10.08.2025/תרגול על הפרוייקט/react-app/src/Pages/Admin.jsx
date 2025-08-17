import React, { useState, useEffect } from 'react';
import {
  Container,
  Typography,
  Box,
  Paper,
  Grid,
  Card,
  CardContent,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  FormControl,
  InputLabel,
  Select,
  MenuItem,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  IconButton,
  Chip,
  Alert,
  CircularProgress,
  Tabs,
  Tab
} from '@mui/material';
import {
  Add,
  Delete,
  Edit,
  Block,
  Save,
  Cancel,
  AdminPanelSettings,
  Refresh
} from '@mui/icons-material';
import { useUser } from '../Contexts/UserContext';
import { useVacations } from '../Contexts/VacationsContext';
import { useNavigate } from 'react-router-dom';
import {
  getAllUsers,
  addVacation,
  deleteVacation,
  updateUserByAdmin,
  deleteUser,
  banUser,
  unbanUser,
  updateVacation,
  uploadVacationImage,
  getVacationImageUrl,
  getCountries
} from '../api/api';

const Admin = () => {
  const { user } = useUser();
  const { vacations, fetchVacations } = useVacations();
  const navigate = useNavigate();
  
  // State
  const [activeTab, setActiveTab] = useState(0);
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [successMessage, setSuccessMessage] = useState('');
  
  // State להוספת חופשה
  const [addVacationDialog, setAddVacationDialog] = useState(false);
  const [vacationForm, setVacationForm] = useState({
    country_id: '',
    vacation_description: '',
    vacation_start: '',
    vacation_ends: '',
    vacation_price: '',
    vacation_file_name: ''
  });
  
  // State לעריכת חופשה
  const [editVacationDialog, setEditVacationDialog] = useState(false);
  const [selectedVacation, setSelectedVacation] = useState(null);
  const [editVacationForm, setEditVacationForm] = useState({
    country_id: '',
    vacation_description: '',
    vacation_start: '',
    vacation_ends: '',
    vacation_price: '',
    vacation_file_name: ''
  });
  
  // State לניהול קבצים
  const [selectedFile, setSelectedFile] = useState(null);
  const [editSelectedFile, setEditSelectedFile] = useState(null);
  
  // State למדינות
  const [countries, setCountries] = useState([]);
  
  // State לעריכת משתמש
  const [editUserDialog, setEditUserDialog] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);
  const [userForm, setUserForm] = useState({
    first_name: '',
    last_name: '',
    user_email: '',
    role_id: ''
  });
  
  // State להרחקת משתמש
  const [banDialog, setBanDialog] = useState(false);
  const [banForm, setBanForm] = useState({
    ban_reason: '',
    ban_until: ''
  });

  // State לאזהרות ספציפיות לכל שדה
  const [fieldErrors, setFieldErrors] = useState({
    country_id: '',
    vacation_description: '',
    vacation_start: '',
    vacation_ends: '',
    vacation_price: ''
  });

  useEffect(() => {
    if (user && user.role_id === 1) {
      fetchUsers();
      fetchCountries();
    }
  }, [user]);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      setError('');
      const usersData = await getAllUsers();
      setUsers(usersData);
    } catch (err) {
      setError('שגיאה בטעינת המשתמשים');
      console.error('Error fetching users:', err);
    } finally {
      setLoading(false);
    }
  };

  const fetchCountries = async () => {
    try {
      setLoading(true);
      setError('');
      const countriesData = await getCountries();
      setCountries(countriesData);
    } catch (err) {
      setError('שגיאה בטעינת המדינות');
      console.error('Error fetching countries:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleRefreshVacations = async () => {
    try {
      setLoading(true);
      setError('');
      setSuccessMessage('');
      await fetchVacations();
      setSuccessMessage('החופשות רועננו בהצלחה');
      setTimeout(() => setSuccessMessage(''), 3000); // הסתר אחרי 3 שניות
    } catch (err) {
      setError('שגיאה ברענון החופשות');
      console.error('Error refreshing vacations:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleRefreshUsers = async () => {
    try {
      setLoading(true);
      setError('');
      setSuccessMessage('');
      await fetchUsers();
      setSuccessMessage('המשתמשים רועננו בהצלחה');
      setTimeout(() => setSuccessMessage(''), 3000); // הסתר אחרי 3 שניות
    } catch (err) {
      setError('שגיאה ברענון המשתמשים');
      console.error('Error refreshing users:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleAddVacation = async () => {
    try {
      // נקה שגיאות קודמות
      setFieldErrors({
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: ''
      });
      
      // ולידציה
      let hasErrors = false;
      const newFieldErrors = {
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: ''
      };
      
      if (!vacationForm.country_id) {
        newFieldErrors.country_id = 'חובה לבחור מדינה';
        hasErrors = true;
      }
      if (!vacationForm.vacation_description.trim()) {
        newFieldErrors.vacation_description = 'חובה למלא תיאור החופשה';
        hasErrors = true;
      }
      if (!vacationForm.vacation_start) {
        newFieldErrors.vacation_start = 'חובה לבחור תאריך התחלה';
        hasErrors = true;
      }
      if (!vacationForm.vacation_ends) {
        newFieldErrors.vacation_ends = 'חובה לבחור תאריך סיום';
        hasErrors = true;
      }
      if (!vacationForm.vacation_price || vacationForm.vacation_price <= 0) {
        newFieldErrors.vacation_price = 'חובה למלא מחיר חיובי';
        hasErrors = true;
      }
      
      if (hasErrors) {
        setFieldErrors(newFieldErrors);
        return;
      }
      
      setLoading(true);
      
      // אם יש קובץ נבחר, העלה אותו קודם
      if (selectedFile) {
        const uploadResult = await uploadVacationImage(selectedFile);
        // עדכן את שם הקובץ בתוצאה
        setVacationForm(prev => ({
          ...prev,
          vacation_file_name: uploadResult.filename
        }));
      }
      
      await addVacation(vacationForm);
      setAddVacationDialog(false);
      setVacationForm({
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: '',
        vacation_file_name: ''
      });
      setSelectedFile(null);
      setFieldErrors({
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: ''
      });
      fetchVacations();
    } catch (err) {
      if (err.message) {
        setError(err.message);
      } else {
        setError('שגיאה בהוספת החופשה');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteVacation = async (vacationId) => {
    if (window.confirm('האם אתה בטוח שברצונך למחוק חופשה זו?')) {
      try {
        setLoading(true);
        await deleteVacation(vacationId);
        fetchVacations();
      } catch (err) {
        setError('שגיאה במחיקת החופשה');
      } finally {
        setLoading(false);
      }
    }
  };

  const handleEditVacation = (vacation) => {
    setSelectedVacation(vacation);
    setEditVacationForm({
      country_id: vacation.country_id || '',
      vacation_description: vacation.vacation_description || '',
      vacation_start: vacation.vacation_start || '',
      vacation_ends: vacation.vacation_ends || '',
      vacation_price: vacation.vacation_price || '',
      vacation_file_name: vacation.vacation_file_name || ''
    });
    setEditSelectedFile(null);
    setEditVacationDialog(true);
    setFieldErrors({
      country_id: '',
      vacation_description: '',
      vacation_start: '',
      vacation_ends: '',
      vacation_price: ''
    });
  };

  const handleUpdateVacation = async () => {
    try {
      // נקה שגיאות קודמות
      setFieldErrors({
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: ''
      });
      
      // ולידציה
      let hasErrors = false;
      const newFieldErrors = {
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: ''
      };
      
      if (!editVacationForm.country_id) {
        newFieldErrors.country_id = 'חובה לבחור מדינה';
        hasErrors = true;
      }
      if (!editVacationForm.vacation_description.trim()) {
        newFieldErrors.vacation_description = 'חובה למלא תיאור החופשה';
        hasErrors = true;
      }
      if (!editVacationForm.vacation_start) {
        newFieldErrors.vacation_start = 'חובה לבחור תאריך התחלה';
        hasErrors = true;
      }
      if (!editVacationForm.vacation_ends) {
        newFieldErrors.vacation_ends = 'חובה לבחור תאריך סיום';
        hasErrors = true;
      }
      if (!editVacationForm.vacation_price || editVacationForm.vacation_price <= 0) {
        newFieldErrors.vacation_price = 'חובה למלא מחיר חיובי';
        hasErrors = true;
      }
      
      if (hasErrors) {
        setFieldErrors(newFieldErrors);
        return;
      }
      
      setLoading(true);
      
      let updatedForm = { ...editVacationForm };
      
      // אם יש קובץ נבחר, העלה אותו קודם
      if (editSelectedFile) {
        const uploadResult = await uploadVacationImage(editSelectedFile);
        updatedForm.vacation_file_name = uploadResult.filename;
      }
      
      await updateVacation(selectedVacation.vacation_id, updatedForm);
      setEditVacationDialog(false);
      setSelectedVacation(null);
      setEditVacationForm({
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: '',
        vacation_file_name: ''
      });
      setEditSelectedFile(null);
      setFieldErrors({
        country_id: '',
        vacation_description: '',
        vacation_start: '',
        vacation_ends: '',
        vacation_price: ''
      });
      fetchVacations();
    } catch (err) {
      if (err.message) {
        setError(err.message);
      } else {
        setError('שגיאה בעדכון החופשה');
      }
    } finally {
      setLoading(false);
    }
  };

  const handleFileChange = (event, isEdit = false) => {
    const file = event.target.files[0];
    if (file) {
      if (isEdit) {
        setEditSelectedFile(file);
        setEditVacationForm(prev => ({
          ...prev,
          vacation_file_name: file.name
        }));
      } else {
        setSelectedFile(file);
        setVacationForm(prev => ({
          ...prev,
          vacation_file_name: file.name
        }));
      }
    }
  };

  const handleEditUser = (user) => {
    setSelectedUser(user);
    setUserForm({
      first_name: user.first_name || '',
      last_name: user.last_name || '',
      user_email: user.user_email || '',
      role_id: user.role_id || ''
    });
    setEditUserDialog(true);
  };

  const handleUpdateUser = async () => {
    try {
      setLoading(true);
      await updateUserByAdmin(selectedUser.user_id, userForm);
      setEditUserDialog(false);
      fetchUsers();
    } catch (err) {
      setError('שגיאה בעדכון המשתמש');
    } finally {
      setLoading(false);
    }
  };

  const handleDeleteUser = async (userId) => {
    if (window.confirm('האם אתה בטוח שברצונך למחוק משתמש זה?')) {
      try {
        setLoading(true);
        await deleteUser(userId);
        fetchUsers();
      } catch (err) {
        setError('שגיאה במחיקת המשתמש');
      } finally {
        setLoading(false);
      }
    }
  };

  const handleBanUser = (user) => {
    setSelectedUser(user);
    setBanForm({
      ban_reason: '',
      ban_until: ''
    });
    setBanDialog(true);
  };

  const handleBanSubmit = async () => {
    try {
      setLoading(true);
      await banUser(selectedUser.user_id, banForm);
      setBanDialog(false);
      fetchUsers();
      setSuccessMessage('המשתמש הורחק בהצלחה');
    } catch (err) {
      setError('שגיאה בהרחקת המשתמש');
    } finally {
      setLoading(false);
    }
  };

  const handleUnbanUser = async (userId) => {
    if (window.confirm('האם אתה בטוח שברצונך לבטל את הרחקת המשתמש?')) {
      try {
        setLoading(true);
        await unbanUser(userId);
        fetchUsers();
        setSuccessMessage('הרחקת המשתמש בוטלה בהצלחה');
      } catch (err) {
        setError('שגיאה בביטול הרחקת המשתמש');
      } finally {
        setLoading(false);
      }
    }
  };

  // בדיקה אם המשתמש הוא אדמין
  if (!user || user.role_id !== 1) {
    return (
      <Container maxWidth="sm" sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center',
        minHeight: '80vh',
        justifyContent: 'center'
      }}>
        <Typography variant="h5" color="text.secondary">
          אין לך הרשאה לגשת לדף זה
        </Typography>
        <Button 
          variant="contained" 
          onClick={() => navigate('/')}
          sx={{ mt: 2 }}
        >
          חזרה לדף הבית
        </Button>
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
          <AdminPanelSettings sx={{ mr: 2, verticalAlign: 'middle' }} />
          ניהול מערכת
        </Typography>
      </Box>

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      {successMessage && (
        <Alert severity="success" sx={{ mb: 3 }}>
          {successMessage}
        </Alert>
      )}

      <Paper sx={{ mb: 3 }}>
        <Tabs 
          value={activeTab} 
          onChange={(e, newValue) => {
            setActiveTab(newValue);
            setError(''); // נקה שגיאות
            setSuccessMessage(''); // נקה הודעות הצלחה
          }}
          sx={{ borderBottom: 1, borderColor: 'divider' }}
        >
          <Tab label="ניהול חופשות" />
          <Tab label="ניהול משתמשים" />
        </Tabs>
      </Paper>

      {activeTab === 0 && (
        <Paper sx={{ p: 3 }}>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
            <Typography variant="h5" sx={{ fontWeight: 'bold' }}>
              ניהול חופשות
            </Typography>
            <Box sx={{ display: 'flex', gap: 2 }}>
              <Button 
                variant="outlined" 
                startIcon={<Refresh />}
                onClick={handleRefreshVacations}
                disabled={loading}
              >
                רענן
              </Button>
              <Button 
                variant="contained" 
                startIcon={<Add />}
                onClick={() => {
                setAddVacationDialog(true);
                setError('');
                setFieldErrors({
                  country_id: '',
                  vacation_description: '',
                  vacation_start: '',
                  vacation_ends: '',
                  vacation_price: ''
                });
                setSuccessMessage('');
              }}
              >
                הוסף חופשה
              </Button>
            </Box>
          </Box>

          <Grid container spacing={3}>
            {vacations.map((vacation) => (
              <Grid size={{ xs: 12, sm: 6, md: 4 }} key={vacation.vacation_id}>
                <Card>
                  <Box
                    component="img"
                    src={getVacationImageUrl(vacation.vacation_file_name)}
                    alt={vacation.country_name}
                    sx={{
                      width: '100%',
                      height: 200,
                      objectFit: 'cover',
                      borderTopLeftRadius: 4,
                      borderTopRightRadius: 4
                    }}
                  />
                  <CardContent>
                    <Typography variant="h6" gutterBottom>
                      {vacation.country_name}
                    </Typography>
                    <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
                      {vacation.vacation_description}
                    </Typography>
                    <Typography variant="body1" color="primary.main" sx={{ fontWeight: 'bold' }}>
                      ₪{vacation.vacation_price}
                    </Typography>
                    <Box sx={{ mt: 2, display: 'flex', gap: 1 }}>
                      <Button 
                        size="small" 
                        variant="outlined" 
                        startIcon={<Edit />}
                        onClick={() => {
                          handleEditVacation(vacation);
                          setError('');
                          setSuccessMessage('');
                        }}
                      >
                        ערוך
                      </Button>
                      <Button 
                        size="small" 
                        variant="outlined" 
                        color="error"
                        startIcon={<Delete />}
                        onClick={() => handleDeleteVacation(vacation.vacation_id)}
                      >
                        מחק
                      </Button>
                    </Box>
                  </CardContent>
                </Card>
              </Grid>
            ))}
          </Grid>
        </Paper>
      )}

      {activeTab === 1 && (
        <Paper sx={{ p: 3 }}>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 3 }}>
            <Typography variant="h5" sx={{ fontWeight: 'bold' }}>
              ניהול משתמשים
            </Typography>
            <Button 
              variant="outlined" 
              startIcon={<Refresh />}
              onClick={handleRefreshUsers}
              disabled={loading}
            >
              רענן
            </Button>
          </Box>

          {loading ? (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 4 }}>
              <CircularProgress />
            </Box>
          ) : (
            <TableContainer>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>שם</TableCell>
                    <TableCell>אימייל</TableCell>
                    <TableCell>תפקיד</TableCell>
                    <TableCell>סטטוס</TableCell>
                    <TableCell>פעולות</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {users.map((user) => (
                    <TableRow key={user.user_id}>
                      <TableCell>
                        {user.first_name && user.last_name 
                          ? `${user.first_name} ${user.last_name}`
                          : 'לא מוגדר'
                        }
                      </TableCell>
                      <TableCell>{user.user_email}</TableCell>
                      <TableCell>
                        <Chip 
                          label={user.role_id === 1 ? 'אדמין' : 'משתמש'} 
                          color={user.role_id === 1 ? 'primary' : 'default'}
                          size="small"
                        />
                      </TableCell>
                      <TableCell>
                        <Chip 
                          label={user.is_banned ? 'מוחרם' : 'פעיל'} 
                          color={user.is_banned ? 'error' : 'success'}
                          size="small"
                        />
                      </TableCell>
                      <TableCell>
                        <Box sx={{ display: 'flex', gap: 1 }}>
                          <IconButton 
                            size="small" 
                            onClick={() => handleEditUser(user)}
                          >
                            <Edit />
                          </IconButton>
                          <IconButton 
                            size="small" 
                            color="error"
                            onClick={() => handleDeleteUser(user.user_id)}
                          >
                            <Delete />
                          </IconButton>
                          {user.is_banned ? (
                            <IconButton 
                              size="small" 
                              color="success"
                              onClick={() => handleUnbanUser(user.user_id)}
                              title="בטל הרחקה"
                            >
                              <Block />
                            </IconButton>
                          ) : (
                            <IconButton 
                              size="small" 
                              color="warning"
                              onClick={() => handleBanUser(user)}
                              title="הרחק משתמש"
                            >
                              <Block />
                            </IconButton>
                          )}
                        </Box>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          )}
        </Paper>
      )}

      {/* דיאלוג הוספת חופשה */}
      <Dialog open={addVacationDialog} onClose={() => {
        setAddVacationDialog(false);
        setFieldErrors({
          country_id: '',
          vacation_description: '',
          vacation_start: '',
          vacation_ends: '',
          vacation_price: ''
        });
      }} maxWidth="md" fullWidth>
        <DialogTitle>הוסף חופשה חדשה</DialogTitle>
        <DialogContent>
          <Grid container spacing={2} sx={{ pt: 2 }}>
            <Grid size={{ xs: 12, sm: 6 }}>
              <FormControl fullWidth error={!!fieldErrors.country_id}>
                <InputLabel>מדינה</InputLabel>
                <Select
                  value={vacationForm.country_id}
                  label="מדינה"
                  onChange={(e) => {
                    setVacationForm({ ...vacationForm, country_id: e.target.value });
                    if (fieldErrors.country_id) {
                      setFieldErrors(prev => ({ ...prev, country_id: '' }));
                    }
                  }}
                >
                  {countries.map((country) => (
                    <MenuItem key={country.country_id} value={country.country_id}>
                      {country.country_name}
                    </MenuItem>
                  ))}
                </Select>
                {fieldErrors.country_id && (
                  <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                    {fieldErrors.country_id}
                  </Typography>
                )}
              </FormControl>
            </Grid>
            <Grid size={{ xs: 12 }}>
              <TextField
                fullWidth
                label="תיאור החופשה"
                value={vacationForm.vacation_description}
                onChange={(e) => {
                  setVacationForm({ ...vacationForm, vacation_description: e.target.value });
                  if (fieldErrors.vacation_description) {
                    setFieldErrors(prev => ({ ...prev, vacation_description: '' }));
                  }
                }}
                variant="outlined"
                multiline
                rows={3}
                error={!!fieldErrors.vacation_description}
              />
              {fieldErrors.vacation_description && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_description}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="תאריך התחלה"
                type="date"
                value={vacationForm.vacation_start}
                onChange={(e) => {
                  setVacationForm({ ...vacationForm, vacation_start: e.target.value });
                  if (fieldErrors.vacation_start) {
                    setFieldErrors(prev => ({ ...prev, vacation_start: '' }));
                  }
                }}
                variant="outlined"
                InputLabelProps={{ shrink: true }}
                error={!!fieldErrors.vacation_start}
              />
              {fieldErrors.vacation_start && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_start}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="תאריך סיום"
                type="date"
                value={vacationForm.vacation_ends}
                onChange={(e) => {
                  setVacationForm({ ...vacationForm, vacation_ends: e.target.value });
                  if (fieldErrors.vacation_ends) {
                    setFieldErrors(prev => ({ ...prev, vacation_ends: '' }));
                  }
                }}
                variant="outlined"
                InputLabelProps={{ shrink: true }}
                error={!!fieldErrors.vacation_ends}
              />
              {fieldErrors.vacation_ends && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_ends}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="מחיר"
                type="number"
                value={vacationForm.vacation_price}
                onChange={(e) => {
                  setVacationForm({ ...vacationForm, vacation_price: e.target.value });
                  if (fieldErrors.vacation_price) {
                    setFieldErrors(prev => ({ ...prev, vacation_price: '' }));
                  }
                }}
                variant="outlined"
                error={!!fieldErrors.vacation_price}
              />
              {fieldErrors.vacation_price && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_price}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <input
                accept="image/*"
                style={{ display: 'none' }}
                id="vacation-image-file"
                type="file"
                onChange={(e) => handleFileChange(e, false)}
              />
              <label htmlFor="vacation-image-file">
                <Button
                  variant="outlined"
                  component="span"
                  fullWidth
                  sx={{ height: '56px' }}
                >
                  {selectedFile ? selectedFile.name : 'בחר תמונה לחופשה'}
                </Button>
              </label>
              {selectedFile && (
                <Typography variant="caption" display="block" sx={{ mt: 1 }}>
                  קובץ נבחר: {selectedFile.name}
                </Typography>
              )}
            </Grid>
          </Grid>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setAddVacationDialog(false)}>
            ביטול
          </Button>
          <Button 
            variant="contained" 
            onClick={handleAddVacation}
            disabled={loading}
          >
            {loading ? 'מוסיף...' : 'הוסף'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* דיאלוג עריכת משתמש */}
      <Dialog open={editUserDialog} onClose={() => setEditUserDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>ערוך משתמש</DialogTitle>
        <DialogContent>
          <Grid container spacing={2} sx={{ pt: 2 }}>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="שם פרטי"
                value={userForm.first_name}
                onChange={(e) => setUserForm({ ...userForm, first_name: e.target.value })}
                variant="outlined"
              />
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="שם משפחה"
                value={userForm.last_name}
                onChange={(e) => setUserForm({ ...userForm, last_name: e.target.value })}
                variant="outlined"
              />
            </Grid>
            <Grid size={{ xs: 12 }}>
              <TextField
                fullWidth
                label="אימייל"
                value={userForm.user_email}
                onChange={(e) => setUserForm({ ...userForm, user_email: e.target.value })}
                variant="outlined"
              />
            </Grid>
            <Grid size={{ xs: 12 }}>
              <FormControl fullWidth>
                <InputLabel>תפקיד</InputLabel>
                <Select
                  value={userForm.role_id}
                  label="תפקיד"
                  onChange={(e) => setUserForm({ ...userForm, role_id: e.target.value })}
                >
                  <MenuItem value={1}>אדמין</MenuItem>
                  <MenuItem value={2}>משתמש</MenuItem>
                </Select>
              </FormControl>
            </Grid>
          </Grid>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditUserDialog(false)}>
            ביטול
          </Button>
          <Button 
            variant="contained" 
            onClick={handleUpdateUser}
            disabled={loading}
          >
            {loading ? 'שומר...' : 'שמור'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* דיאלוג הרחקת משתמש */}
      <Dialog open={banDialog} onClose={() => setBanDialog(false)} maxWidth="sm" fullWidth>
        <DialogTitle>הרחק משתמש</DialogTitle>
        <DialogContent>
          <Grid container spacing={2} sx={{ pt: 2 }}>
            <Grid size={{ xs: 12 }}>
              <TextField
                fullWidth
                label="סיבת ההרחקה"
                value={banForm.ban_reason}
                onChange={(e) => setBanForm({ ...banForm, ban_reason: e.target.value })}
                variant="outlined"
                multiline
                rows={3}
              />
            </Grid>
            <Grid size={{ xs: 12 }}>
              <TextField
                fullWidth
                label="תאריך סיום ההרחקה"
                type="datetime-local"
                value={banForm.ban_until}
                onChange={(e) => setBanForm({ ...banForm, ban_until: e.target.value })}
                variant="outlined"
                InputLabelProps={{ shrink: true }}
              />
            </Grid>
          </Grid>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setBanDialog(false)}>
            ביטול
          </Button>
          <Button 
            variant="contained" 
            color="error"
            onClick={handleBanSubmit}
            disabled={loading}
          >
            {loading ? 'מרחיק...' : 'הרחק'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* דיאלוג עריכת חופשה */}
      <Dialog open={editVacationDialog} onClose={() => {
        setEditVacationDialog(false);
        setFieldErrors({
          country_id: '',
          vacation_description: '',
          vacation_start: '',
          vacation_ends: '',
          vacation_price: ''
        });
      }} maxWidth="md" fullWidth>
        <DialogTitle>ערוך חופשה</DialogTitle>
        <DialogContent>
          <Grid container spacing={2} sx={{ pt: 2 }}>
            <Grid size={{ xs: 12, sm: 6 }}>
              <FormControl fullWidth error={!!fieldErrors.country_id}>
                <InputLabel>מדינה</InputLabel>
                <Select
                  value={editVacationForm.country_id}
                  label="מדינה"
                  onChange={(e) => {
                    setEditVacationForm({ ...editVacationForm, country_id: e.target.value });
                    if (fieldErrors.country_id) {
                      setFieldErrors(prev => ({ ...prev, country_id: '' }));
                    }
                  }}
                >
                  {countries.map((country) => (
                    <MenuItem key={country.country_id} value={country.country_id}>
                      {country.country_name}
                    </MenuItem>
                  ))}
                </Select>
                {fieldErrors.country_id && (
                  <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                    {fieldErrors.country_id}
                  </Typography>
                )}
              </FormControl>
            </Grid>
            <Grid size={{ xs: 12 }}>
              <TextField
                fullWidth
                label="תיאור החופשה"
                value={editVacationForm.vacation_description}
                onChange={(e) => {
                  setEditVacationForm({ ...editVacationForm, vacation_description: e.target.value });
                  if (fieldErrors.vacation_description) {
                    setFieldErrors(prev => ({ ...prev, vacation_description: '' }));
                  }
                }}
                variant="outlined"
                multiline
                rows={3}
                error={!!fieldErrors.vacation_description}
              />
              {fieldErrors.vacation_description && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_description}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="תאריך התחלה"
                type="date"
                value={editVacationForm.vacation_start}
                onChange={(e) => {
                  setEditVacationForm({ ...editVacationForm, vacation_start: e.target.value });
                  if (fieldErrors.vacation_start) {
                    setFieldErrors(prev => ({ ...prev, vacation_start: '' }));
                  }
                }}
                variant="outlined"
                InputLabelProps={{ shrink: true }}
                error={!!fieldErrors.vacation_start}
              />
              {fieldErrors.vacation_start && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_start}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="תאריך סיום"
                type="date"
                value={editVacationForm.vacation_ends}
                onChange={(e) => {
                  setEditVacationForm({ ...editVacationForm, vacation_ends: e.target.value });
                  if (fieldErrors.vacation_ends) {
                    setFieldErrors(prev => ({ ...prev, vacation_ends: '' }));
                  }
                }}
                variant="outlined"
                InputLabelProps={{ shrink: true }}
                error={!!fieldErrors.vacation_ends}
              />
              {fieldErrors.vacation_ends && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_ends}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <TextField
                fullWidth
                label="מחיר"
                type="number"
                value={editVacationForm.vacation_price}
                onChange={(e) => {
                  setEditVacationForm({ ...editVacationForm, vacation_price: e.target.value });
                  if (fieldErrors.vacation_price) {
                    setFieldErrors(prev => ({ ...prev, vacation_price: '' }));
                  }
                }}
                variant="outlined"
                error={!!fieldErrors.vacation_price}
              />
              {fieldErrors.vacation_price && (
                <Typography variant="caption" color="error" sx={{ mt: 0.5 }}>
                  {fieldErrors.vacation_price}
                </Typography>
              )}
            </Grid>
            <Grid size={{ xs: 12, sm: 6 }}>
              <input
                accept="image/*"
                style={{ display: 'none' }}
                id="edit-vacation-image-file"
                type="file"
                onChange={(e) => handleFileChange(e, true)}
              />
              <label htmlFor="edit-vacation-image-file">
                <Button
                  variant="outlined"
                  component="span"
                  fullWidth
                  sx={{ height: '56px' }}
                >
                  {editSelectedFile ? editSelectedFile.name : 'בחר תמונה חדשה (אופציונלי)'}
                </Button>
              </label>
                             {editSelectedFile && (
                 <Typography variant="caption" display="block" sx={{ mt: 1 }}>
                   קובץ נבחר: {editSelectedFile.name}
                 </Typography>
               )}
               {!editSelectedFile && editVacationForm.vacation_file_name && (
                 <Typography variant="caption" display="block" sx={{ mt: 1 }}>
                   תמונה נוכחית: {editVacationForm.vacation_file_name}
                 </Typography>
               )}
            </Grid>
          </Grid>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditVacationDialog(false)}>
            ביטול
          </Button>
          <Button 
            variant="contained" 
            onClick={handleUpdateVacation}
            disabled={loading}
          >
            {loading ? 'שומר...' : 'שמור שינויים'}
          </Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default Admin;
