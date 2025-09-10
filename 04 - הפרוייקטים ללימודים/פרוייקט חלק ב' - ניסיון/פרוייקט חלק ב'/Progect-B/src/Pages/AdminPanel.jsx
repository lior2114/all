import React, { useEffect, useState } from 'react';
import { Container, Box, Paper, Typography, Alert, Grid, Button, Divider, List, ListItem, ListItemText, Dialog, DialogTitle, DialogContent, DialogActions, TextField } from '@mui/material';
import { UseUser } from '../Contexts/UserContexts';
import { useNavigate } from 'react-router-dom';
import { useUi } from '../Contexts/UiContext';
import { getVacations, deleteVacation, getUsers, updateUser, deleteUser, banUser, unbanUser, checkBan } from '../api/api';
import styles from './AdminPanel.module.css';

export function AdminPanel() {
  const { user, isAuthenticated } = UseUser();
  const { language } = useUi();
  const navigate = useNavigate();

  const [vacations, setVacations] = useState([]);
  const [users, setUsers] = useState([]);
  const [bans, setBans] = useState({}); // userId -> ban info
  const [error, setError] = useState('');

  const [banOpen, setBanOpen] = useState(false);
  const [banTarget, setBanTarget] = useState(null);
  const [banReason, setBanReason] = useState('');
  const [banDays, setBanDays] = useState('7');

  const t = (he, en) => (language === 'he' ? he : en);

  useEffect(() => {
    if (!isAuthenticated || user?.role_id !== 1) return;
    const load = async () => {
      try {
        const [v, u] = await Promise.all([getVacations(), getUsers()]);
        setVacations(Array.isArray(v) ? v : []);
        setUsers(Array.isArray(u) ? u : []);
        // Preload ban status
        const entries = await Promise.all((Array.isArray(u) ? u : []).map(async (usr) => {
          try { const info = await checkBan(usr.user_id); return [usr.user_id, info]; } catch { return [usr.user_id, { banned: false }]; }
        }));
        const map = {};
        entries.forEach(([id, info]) => { map[id] = info; });
        setBans(map);
      } catch (e) {
        setError(e.message || 'Failed to load admin data');
      }
    };
    load();
  }, [isAuthenticated, user]);

  if (!isAuthenticated || user?.role_id !== 1) {
    return (
      <Container maxWidth="md">
        <Box sx={{ mt: 4 }}>
          <Alert severity="error" className={styles.errorAlert}>
            {t('אין לך הרשאה לצפות בדף זה', 'You do not have permission to view this page.')}
          </Alert>
        </Box>
      </Container>
    );
  }

  const handleDeleteVacation = async (id) => {
    if (!window.confirm(t('האם אתה בטוח שברצונך למחוק את החופשה? פעולה זו בלתי הפיכה!', 'Are you sure you want to delete this vacation? This action is irreversible!'))) return;
    try {
      await deleteVacation(id, user?.user_id);
      setVacations(prev => prev.filter(v => Number(v.vacation_id) !== Number(id)));
    } catch (e) {
      setError(e.message || 'Failed to delete vacation');
    }
  };

  const handleToggleAdmin = async (u) => {
    const nextRole = Number(u.role_id) === 1 ? 2 : 1;
    try {
      await updateUser(u.user_id, { role_id: nextRole });
      setUsers(prev => prev.map(x => x.user_id === u.user_id ? { ...x, role_id: nextRole } : x));
    } catch (e) {
      setError(e.message || 'Failed to update user');
    }
  };

  const handleDeleteUser = async (u) => {
    try {
      if (!window.confirm(t('האם למחוק את המשתמש?', 'Delete this user?'))) return;
      await deleteUser(u.user_id);
      setUsers(prev => prev.filter(x => x.user_id !== u.user_id));
    } catch (e) {
      setError(e.message || 'Failed to delete user');
    }
  };

  const openBanDialog = (u) => {
    setBanTarget(u);
    setBanReason('');
    setBanDays('7');
    setBanOpen(true);
  };

  const submitBan = async () => {
    const days = parseInt(banDays, 10) || 0;
    if (!banTarget || days <= 0) { setBanOpen(false); return; }
    try {
      await banUser(banTarget.user_id, { reason: banReason, days });
      setBanOpen(false);
      const info = await checkBan(banTarget.user_id);
      setBans(prev => ({ ...prev, [banTarget.user_id]: info }));
    } catch (e) {
      setError(e.message || 'Failed to ban user');
      setBanOpen(false);
    }
  };

  const handleUnban = async (u) => {
    try {
      await unbanUser(u.user_id);
      setBans(prev => ({ ...prev, [u.user_id]: { banned: false, info: null } }));
    } catch (e) {
      setError(e.message || 'Failed to unban user');
    }
  }

  return (
    <Container maxWidth="lg" className={styles.adminContainer}>
      <Box sx={{ mt: 4 }}>
        {error && <Alert severity="error" className={styles.errorAlert}>{error}</Alert>}
        <Grid container spacing={3} className={styles.adminGrid}>
          <Grid item xs={12} sm={6} className="admin-vacations">
            <Paper elevation={3} className={styles.adminSection}>
              <Box className={styles.adminSectionHeader}>
                <Typography variant="h6" className={styles.adminSectionTitle}>
                  {t('ניהול חופשות', 'Vacations Management')} ({vacations.length})
                </Typography>
                <Button variant="contained" onClick={() => navigate('/vacations/add')}>
                  {t('הוסף חופשה', 'Add Vacation')}
                </Button>
              </Box>
              <Divider className={styles.adminSectionDivider} />
              <List className={styles.adminList}>
                {vacations.map(v => (
                  <ListItem key={v.vacation_id} className={styles.adminListItem}>
                    <ListItemText 
                      primary={v.country_name} 
                      secondary={`${v.vacation_start} - ${v.vacation_ends}`}
                      className={styles.adminListItemText}
                    />
                    <Box className={styles.adminActions}>
                      <Button className={styles.editButton} size="small" onClick={() => navigate(`/vacations/edit/${v.vacation_id}`)}>{t('ערוך', 'Edit')}</Button>
                      <Button className={styles.deleteButton} size="small" onClick={() => handleDeleteVacation(v.vacation_id)}>{t('מחק', 'Delete')}</Button>
                    </Box>
                  </ListItem>
                ))}
              </List>
            </Paper>
          </Grid>

          <Grid item xs={12} sm={6} className="admin-users">
            <Paper elevation={3} className={styles.adminSection}>
              <Typography variant="h6" className={styles.adminSectionTitle}>
                {t('ניהול משתמשים', 'Users Management')} ({users.length})
              </Typography>
              <Divider className={styles.adminSectionDivider} />
              <List className={styles.adminList}>
                {users.map(u => (
                  <ListItem key={u.user_id} className={styles.adminListItem}>
                    <ListItemText 
                      primary={`${u.first_name} ${u.last_name}`} 
                      secondary={u.user_email}
                      className={styles.adminListItemText}
                    />
                    <Box className={styles.adminActions}>
                      <Button className={styles.editButton} size="small" onClick={() => handleToggleAdmin(u)}>
                        {Number(u.role_id) === 1 ? t('הסר מנהל', 'Revoke Admin') : t('הפוך למנהל', 'Make Admin')}
                      </Button>
                      {bans[u.user_id]?.banned ? (
                        <Button className={styles.editButton} size="small" onClick={() => handleUnban(u)}>
                          {t('בטל הרחקה', 'Unban')}
                        </Button>
                      ) : (
                        <Button className={styles.banButton} size="small" onClick={() => openBanDialog(u)}>
                          {t('הרחק', 'Ban')}
                        </Button>
                      )}
                      <Button className={styles.deleteButton} size="small" onClick={() => handleDeleteUser(u)} disabled={u.user_id === user?.user_id}>
                        {t('מחק', 'Delete')}
                      </Button>
                    </Box>
                  </ListItem>
                ))}
              </List>
            </Paper>
          </Grid>
        </Grid>
      </Box>

      <Dialog open={banOpen} onClose={() => setBanOpen(false)} fullWidth maxWidth="sm" className={styles.banDialog}>
        <DialogTitle className={styles.banDialogTitle}>{t('הרחקת משתמש', 'Ban user')}</DialogTitle>
        <DialogContent className={styles.banDialogContent}>
          <Box className={styles.banDialogForm}>
            <TextField
              label={t('סיבה', 'Reason')}
              value={banReason}
              onChange={e => setBanReason(e.target.value)}
              fullWidth
            />
            <TextField
              label={t('מספר ימים', 'Days')}
              type="number"
              inputProps={{ min: 1 }}
              value={banDays}
              onChange={e => setBanDays(e.target.value)}
              fullWidth
            />
          </Box>
        </DialogContent>
        <DialogActions className={styles.banDialogActions}>
          <Button onClick={() => setBanOpen(false)}>{t('בטל', 'Cancel')}</Button>
          <Button className={styles.banButton} onClick={submitBan}>{t('הרחק', 'Ban')}</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
}
