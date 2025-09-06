import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { useLanguage } from '../contexts/LanguageContext';
import AdminApi from '../api/adminApi';
import './AdminPanel.css';

const AdminPanel = () => {
  const [users, setUsers] = useState([]);
  const [dashboardData, setDashboardData] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [selectedUser, setSelectedUser] = useState(null);
  const [showBanModal, setShowBanModal] = useState(false);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [banData, setBanData] = useState({
    reason: '',
    banUntil: '',
    isPermanent: false
  });
  const [isLoadingAction, setIsLoadingAction] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  
  const { user } = useAuth();
  const { texts, isRTL } = useLanguage();

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setIsLoading(true);
      const [usersData, dashboardData] = await Promise.all([
        AdminApi.getAllUsers(),
        AdminApi.getAdminDashboard()
      ]);
      setUsers(usersData);
      setDashboardData(dashboardData);
    } catch (error) {
    } finally {
      setIsLoading(false);
    }
  };

  const handleBanUser = async () => {
    if (!selectedUser || !banData.reason.trim()) return;

    setIsLoadingAction(true);
    try {
      const banUntil = banData.isPermanent ? null : banData.banUntil;
      const result = await AdminApi.banUser(selectedUser.user_id, banData.reason, banUntil, user.user_id);
      
      // רענון מיידי של הנתונים
      await loadData();
      setShowBanModal(false);
      setSelectedUser(null);
      setBanData({ reason: '', banUntil: '', isPermanent: false });
      setSuccessMessage(isRTL ? 'המשתמש הורחק בהצלחה!' : 'User banned successfully!');
      setTimeout(() => setSuccessMessage(''), 3000);
    } catch (error) {
      let errorMessage = error.message;
      
      // תרגום שגיאות נפוצות
      if (error.message.includes('Failed to fetch')) {
        errorMessage = isRTL ? 'בעיית חיבור לשרת. אנא בדוק שהשרת רץ ונסה שוב.' : 'Server connection error. Please check if the server is running and try again.';
      } else if (error.message.includes('NetworkError')) {
        errorMessage = isRTL ? 'בעיית רשת. אנא בדוק את החיבור לאינטרנט ונסה שוב.' : 'Network error. Please check your internet connection and try again.';
      }
      
      alert(isRTL ? 'שגיאה בהרחקת המשתמש: ' + errorMessage : 'Error banning user: ' + errorMessage);
    } finally {
      setIsLoadingAction(false);
    }
  };

  const handleUnbanUser = async (userId) => {
    setIsLoadingAction(true);
    try {
      await AdminApi.unbanUser(userId, user.id);
      await loadData();
    } catch (error) {
      console.error('Error unbanning user:', error);
    } finally {
      setIsLoadingAction(false);
    }
  };

  const handleDeleteUser = async () => {
    if (!selectedUser) return;

    setIsLoadingAction(true);
    try {
      await AdminApi.deleteUser(selectedUser.user_id);
      await loadData();
      setShowDeleteModal(false);
      setSelectedUser(null);
    } catch (error) {
      console.error('Error deleting user:', error);
    } finally {
      setIsLoadingAction(false);
    }
  };

  const openBanModal = (user) => {
    setSelectedUser(user);
    setBanData({ reason: '', banUntil: '', isPermanent: false });
    setShowBanModal(true);
  };

  const openDeleteModal = (user) => {
    setSelectedUser(user);
    setShowDeleteModal(true);
  };

  const formatDate = (dateString) => {
    if (!dateString) return '-';
    try {
      const date = new Date(dateString);
      if (isNaN(date.getTime())) {
        console.error('Invalid date:', dateString);
        return dateString;
      }
      return date.toLocaleDateString(isRTL ? 'he-IL' : 'en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      });
    } catch (error) {
      console.error('Error formatting date:', dateString, error);
      return dateString;
    }
  };

  const getRoleDisplayName = (roleName) => {
    switch (roleName) {
      case 'admin':
        return isRTL ? 'מנהל' : 'Admin';
      case 'moderator':
        return isRTL ? 'מנחה' : 'Moderator';
      case 'user':
        return isRTL ? 'משתמש' : 'User';
      default:
        return roleName;
    }
  };

  if (isLoading) {
    return (
      <div className="admin-loading">
        <div className="spinner"></div>
        <p>{isRTL ? 'טוען נתונים...' : 'Loading data...'}</p>
      </div>
    );
  }

  return (
    <div className="admin-container">
      <div className="admin-content">
        <div className="admin-header">
          <h1>{isRTL ? 'פאנל ניהול' : 'Admin Panel'}</h1>
          {successMessage && (
            <div className="success-message">
              ✅ {successMessage}
            </div>
          )}
        </div>

        {/* Dashboard Stats */}
        {dashboardData && (
          <div className="dashboard-stats">
            <div className="stat-card">
              <div className="stat-icon">👥</div>
              <div className="stat-info">
                <h3>{isRTL ? 'סה"כ משתמשים' : 'Total Users'}</h3>
                <p className="stat-value">{dashboardData.total_users}</p>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon">🚫</div>
              <div className="stat-info">
                <h3>{isRTL ? 'משתמשים מוחרמים' : 'Banned Users'}</h3>
                <p className="stat-value">{dashboardData.banned_users}</p>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon">🆕</div>
              <div className="stat-info">
                <h3>{isRTL ? 'משתמשים חדשים היום' : 'New Users Today'}</h3>
                <p className="stat-value">{dashboardData.new_users_today}</p>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon">📚</div>
              <div className="stat-info">
                <h3>{isRTL ? 'שיעורים שהושלמו היום' : 'Lessons Completed Today'}</h3>
                <p className="stat-value">{dashboardData.lessons_completed_today}</p>
              </div>
            </div>

            <div className="stat-card">
              <div className="stat-icon">🔥</div>
              <div className="stat-info">
                <h3>{isRTL ? 'משתמשים פעילים' : 'Active Users'}</h3>
                <p className="stat-value">{dashboardData.active_users}</p>
              </div>
            </div>
          </div>
        )}

        {/* Users Table */}
        <div className="users-section">
          <div className="section-header">
            <h2>{isRTL ? 'ניהול משתמשים' : 'User Management'}</h2>
            <button className="refresh-button" onClick={loadData}>
              🔄 {isRTL ? 'רענן' : 'Refresh'}
            </button>
          </div>

          <div className="users-table-container">
            <table className="users-table">
              <thead>
                <tr>
                  <th>{isRTL ? 'שם' : 'Name'}</th>
                  <th>{isRTL ? 'אימייל' : 'Email'}</th>
                  <th>{isRTL ? 'תפקיד' : 'Role'}</th>
                  <th>{isRTL ? 'תאריך הצטרפות' : 'Join Date'}</th>
                  <th>{isRTL ? 'סטטוס' : 'Status'}</th>
                  <th>{isRTL ? 'פעולות' : 'Actions'}</th>
                </tr>
              </thead>
              <tbody>
                {users.map((userItem) => (
                  <tr key={userItem.user_id} className={userItem.is_banned ? 'banned-user' : ''}>

                    <td>
                      <div className="user-name">
                        {userItem.first_name} {userItem.last_name}
                      </div>
                    </td>
                    <td>{userItem.user_email}</td>
                    <td>
                      <span className={`role-badge role-${userItem.role_name}`}>
                        {getRoleDisplayName(userItem.role_name)}
                      </span>
                    </td>
                    <td>{formatDate(userItem.created_at)}</td>
                    <td>
                      {userItem.is_banned ? (
                        <div className="ban-status">
                          <span className="status-badge banned">
                            {isRTL ? 'מוחרם' : 'Banned'}
                          </span>
                          {userItem.ban_until ? (
                            <div className="ban-details">
                              <small>{isRTL ? 'עד:' : 'Until:'} {formatDate(userItem.ban_until)}</small>
                            </div>
                          ) : (
                            <div className="ban-details">
                              <small>{isRTL ? 'הרחקה קבועה' : 'Permanent'}</small>
                            </div>
                          )}
                          {userItem.ban_reason && (
                            <div className="ban-details">
                              <small>{isRTL ? 'סיבה:' : 'Reason:'} {userItem.ban_reason}</small>
                            </div>
                          )}
                        </div>
                      ) : (
                        <span className="status-badge active">
                          {isRTL ? 'פעיל' : 'Active'}
                        </span>
                      )}
                    </td>
                    <td>
                      <div className="action-buttons">
                        {userItem.is_banned ? (
                          <button
                            className="action-button unban"
                            onClick={() => handleUnbanUser(userItem.user_id)}
                            disabled={isLoadingAction}
                          >
                            {isRTL ? 'בטל הרחקה' : 'Unban'}
                          </button>
                        ) : (
                          <button
                            className="action-button ban"
                            onClick={() => openBanModal(userItem)}
                            disabled={isLoadingAction || userItem.user_id === user.id}
                          >
                            {isRTL ? 'הרחק' : 'Ban'}
                          </button>
                        )}
                        
                        <button
                          className="action-button delete"
                          onClick={() => openDeleteModal(userItem)}
                          disabled={isLoadingAction || userItem.user_id === user.id}
                        >
                          {isRTL ? 'מחק' : 'Delete'}
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>

      {/* Ban Modal */}
      {showBanModal && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <h3>{isRTL ? 'הרחקת משתמש' : 'Ban User'}</h3>
              <button
                className="modal-close"
                onClick={() => setShowBanModal(false)}
              >
                ✕
              </button>
            </div>
            <div className="modal-content">
              <p>
                {isRTL ? 'הרחקת משתמש:' : 'Ban user:'} <strong>{selectedUser?.first_name} {selectedUser?.last_name}</strong>
              </p>
              
              <div className="form-group">
                <label htmlFor="banReason">
                  {isRTL ? 'סיבת ההרחקה:' : 'Ban Reason:'}
                </label>
                <textarea
                  id="banReason"
                  value={banData.reason}
                  onChange={(e) => setBanData(prev => ({ ...prev, reason: e.target.value }))}
                  placeholder={isRTL ? 'הכנס סיבת ההרחקה...' : 'Enter ban reason...'}
                  rows="3"
                />
              </div>

              <div className="form-group">
                <label className="permanent-ban-label">
                  <input
                    type="checkbox"
                    checked={banData.isPermanent}
                    onChange={(e) => setBanData(prev => ({ ...prev, isPermanent: e.target.checked }))}
                    className="permanent-ban-checkbox"
                  />
                  <span className="permanent-ban-text">
                    {isRTL ? 'הרחקה קבועה' : 'Permanent ban'}
                  </span>
                </label>
              </div>

              {!banData.isPermanent && (
                <div className="form-group">
                  <label htmlFor="banUntil">
                    {isRTL ? 'תאריך סיום הרחקה:' : 'Ban until:'}
                  </label>
                  <input
                    type="datetime-local"
                    id="banUntil"
                    value={banData.banUntil}
                    onChange={(e) => setBanData(prev => ({ ...prev, banUntil: e.target.value }))}
                  />
                </div>
              )}

              <div className="modal-actions">
                <button
                  className="modal-button confirm"
                  onClick={handleBanUser}
                  disabled={isLoadingAction || !banData.reason.trim()}
                >
                  {isLoadingAction ? (
                    <span className="loading-spinner">
                      <div className="spinner"></div>
                      {isRTL ? 'מרחיק...' : 'Banning...'}
                    </span>
                  ) : (
                    isRTL ? 'הרחק' : 'Ban'
                  )}
                </button>
                <button
                  className="modal-button cancel"
                  onClick={() => setShowBanModal(false)}
                  disabled={isLoadingAction}
                >
                  {isRTL ? 'ביטול' : 'Cancel'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Delete Modal */}
      {showDeleteModal && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <h3>{isRTL ? 'מחיקת משתמש' : 'Delete User'}</h3>
              <button
                className="modal-close"
                onClick={() => setShowDeleteModal(false)}
              >
                ✕
              </button>
            </div>
            <div className="modal-content">
              <div className="warning-message">
                ⚠️ {isRTL ? 'פעולה זו אינה הפיכה!' : 'This action is irreversible!'}
              </div>
              <p>
                {isRTL ? 'האם אתה בטוח שברצונך למחוק את המשתמש:' : 'Are you sure you want to delete the user:'}
                <br />
                <strong>{selectedUser?.first_name} {selectedUser?.last_name}</strong>
                <br />
                <em>{selectedUser?.user_email}</em>
              </p>

              <div className="modal-actions">
                <button
                  className="modal-button delete"
                  onClick={handleDeleteUser}
                  disabled={isLoadingAction}
                >
                  {isLoadingAction ? (
                    <span className="loading-spinner">
                      <div className="spinner"></div>
                      {isRTL ? 'מוחק...' : 'Deleting...'}
                    </span>
                  ) : (
                    isRTL ? 'מחק' : 'Delete'
                  )}
                </button>
                <button
                  className="modal-button cancel"
                  onClick={() => setShowDeleteModal(false)}
                  disabled={isLoadingAction}
                >
                  {isRTL ? 'ביטול' : 'Cancel'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AdminPanel;
