import * as React from 'react';
import { useState, useEffect } from 'react';
import { styled } from '@mui/material/styles';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Collapse from '@mui/material/Collapse';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Chip from '@mui/material/Chip';
import Button from '@mui/material/Button';
import { red, green, blue } from '@mui/material/colors';
import FavoriteIcon from '@mui/icons-material/Favorite';
import ShareIcon from '@mui/icons-material/Share';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import DeleteIcon from '@mui/icons-material/Delete';
import LocationOnIcon from '@mui/icons-material/LocationOn';
import CalendarTodayIcon from '@mui/icons-material/CalendarToday';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import { useVacation } from '../Contexts/vacationContext';
import { likesContext, useLike } from '../Contexts/likescontext';
import { useUser } from '../Contexts/userContext';
import styles from './vacationCard.module.css';

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme }) => ({
  marginLeft: 'auto',
  transition: theme.transitions.create('transform', {
    duration: theme.transitions.duration.shortest,
  }),
  variants: [
    {
      props: ({ expand }) => !expand,
      style: {
        transform: 'rotate(0deg)',
      },
    },
    {
      props: ({ expand }) => !!expand,
      style: {
        transform: 'rotate(180deg)',
      },
    },
  ],
}));

export function vacationscard() {
    const {addlike, unlike} = useLike()
    const {user} = useUser()
    const { getVacation, deleteVacation } = useVacation();
    const [vacations, setVacations] = useState([]);
    const [expandedCards, setExpandedCards] = useState({});
    const [likedCards, setLikedCards] = useState({});
    const [deleteError, setDeleteError] = useState("");
    
    useEffect(() => {
        const fetchVacations = async () => {
            try {
                const result = await getVacation();
                if (result) {
                    setVacations(result);
                }
            } catch (error) {
                console.error("Failed to fetch vacations:", error);
            }
        };
        fetchVacations();
    }, [getVacation]);

    const handleExpandClick = (index) => {
        setExpandedCards(prev => ({
            ...prev,
            [index]: !prev[index]
        }));
    };


    const handleLikeToggle = async (vacation_id) => {
        if (!user || !user.user_id) {
            alert("need to sign in to like")
            return
        }
        
        const isCurrentlyLiked = likedCards[vacation_id]
        
        try {
            let response
            if (isCurrentlyLiked && user && user.user_id) {
                // אם כבר לייק, אז אנלייק
                response = await unlike(user.user_id, vacation_id)
                if (response) {
                    setLikedCards(prev => ({
                        ...prev,
                        [vacation_id]: false
                    }))
                }
            } else if (user && user.user_id) {
                // אם לא לייק, אז לייק
                response = await addlike(user.user_id, vacation_id)
                if (response) {
                    setLikedCards(prev => ({
                        ...prev,
                        [vacation_id]: true
                    }))
                }
            }
            return response
        } catch (err) {
            console.error(err)
            throw err
        }
    }
    const handledelete = async (id, vacationName) => {
        // אישור מחיקה
        const confirmDelete = window.confirm(`האם אתה בטוח שברצונך למחוק את החופשה "${vacationName}"?`);
        if (!confirmDelete) return;

        try {
            const response = await deleteVacation(id)
            // בדיקה אם יש message של הצלחה במחיקה
            if (response && (response.Message || response.message)) {
                // מחק את החופשה מהרשימה המקומית
                setVacations(prev => prev.filter(vacation => vacation.vacation_id !== id))
                setDeleteError("") // נקה שגיאות קודמות
                console.log("Vacation deleted successfully:", response.Message || response.message)
            } else if (response && (response.Massages)) {
                // אם יש שגיאה מהשרת
                setDeleteError(response.Massages)
            } else {
                setDeleteError("Can't delete vacation - unknown error")
            }
        } catch(err) {
            console.error("Delete error:", err)
            setDeleteError("Error deleting vacation: " + err.message)
        }
    }

    const formatDate = (dateString) => {
        if (!dateString) return 'N/A';
        const date = new Date(dateString);
        return date.toLocaleDateString('he-IL', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    const getCountryInitial = (countryName) => {
        if (!countryName) return 'V';
        return countryName.charAt(0).toUpperCase();
    };

    const getCountryColor = (countryName) => {
        const colors = [red[500], green[500], blue[500]];
        const index = countryName ? countryName.length % colors.length : 0;
        return colors[index];
    };

    return (
        <div className={styles.vacationsContainer}>
            {deleteError && (
                <div style={{ color: 'red', backgroundColor: '#ffebee', padding: '10px', margin: '10px 0', borderRadius: '4px' }}>
                    שגיאה במחיקה: {deleteError}
                    <button onClick={() => setDeleteError("")} style={{ marginLeft: '10px', cursor: 'pointer' }}>✕</button>
                </div>
            )}
            {vacations.map((vacation, index) => (
                <Card key={vacation.vacation_id || index} sx={{ width: '100%' }} className={styles.vacationCard}>
                    <CardHeader
                        avatar={
                            <Avatar sx={{ bgcolor: getCountryColor(vacation.country_name) }} aria-label="country">
                                {getCountryInitial(vacation.country_name)}
                            </Avatar>
                        }
                        action={
                            <IconButton aria-label="settings">
                                <MoreVertIcon />
                            </IconButton>
                        }
                        title={vacation.vacation_name}
                        subheader={vacation.country_name}
                    />
                    {vacation.vacation_file_name && (
                        <CardMedia
                            component="img"
                            height="200"
                            image={vacation.vacation_file_name}
                            alt={vacation.vacation_name}
                            className={styles.cardImage}
                        />
                    )}
                    <CardContent>
                        <Typography variant="body2" sx={{ color: 'text.secondary', marginBottom: 2 }}>
                            {vacation.vacation_description}
                        </Typography>
                        <div className={styles.vacationDetails}>
                            <Chip
                                icon={<LocationOnIcon />}
                                label={vacation.country_name}
                                variant="outlined"
                                size="small"
                                sx={{ margin: 0.5 }}
                            />
                            <Chip
                                icon={<CalendarTodayIcon />}
                                label={`${formatDate(vacation.vacation_start)} - ${formatDate(vacation.vacation_ends)}`}
                                variant="outlined"
                                size="small"
                                sx={{ margin: 0.5 }}
                            />
                            <Chip
                                icon={<AttachMoneyIcon />}
                                label={`₪${vacation.vacation_price.toLocaleString()}`}
                                variant="outlined"
                                color="success"
                                size="small"
                                sx={{ margin: 0.5 }}
                            />
                        </div>
                    </CardContent>
                    <CardActions disableSpacing>
                    <IconButton 
                        aria-label="add to favorites"
                        onClick={() => handleLikeToggle(vacation.vacation_id)}
                        sx={{ color: likedCards[vacation.vacation_id] ? red[500] : 'inherit' }}
                    >
                        <FavoriteIcon />
                    </IconButton>
                    <IconButton aria-label="share">
                        <ShareIcon />
                    </IconButton>
                        {user && user.role_id === 1 && (
                            <Button
                                variant="outlined"
                                color="error"
                                size="small"
                                startIcon={<DeleteIcon />}
                                onClick={() => handledelete(vacation.vacation_id, vacation.vacation_name)}
                                sx={{ marginLeft: 1 }}
                            >
                                מחק
                            </Button>
                        )}
                        <ExpandMore
                            expand={expandedCards[index] || false}
                            onClick={() => handleExpandClick(index)}
                            aria-expanded={expandedCards[index] || false}
                            aria-label="show more"
                        >
                            <ExpandMoreIcon />
                        </ExpandMore>
                    </CardActions>
                    <Collapse in={expandedCards[index] || false} timeout="auto" unmountOnExit>
                        <CardContent>
                            <Typography sx={{ marginBottom: 2, fontWeight: 'bold' }}>
                                פרטי החופשה:
                            </Typography>
                            <Typography sx={{ marginBottom: 1 }}>
                                <strong>מדינה:</strong> {vacation.country_name}
                            </Typography>
                            <Typography sx={{ marginBottom: 1 }}>
                                <strong>תאריך התחלה:</strong> {formatDate(vacation.vacation_start)}
                            </Typography>
                            <Typography sx={{ marginBottom: 1 }}>
                                <strong>תאריך סיום:</strong> {formatDate(vacation.vacation_ends)}
                            </Typography>
                            <Typography sx={{ marginBottom: 1 }}>
                                <strong>מחיר:</strong> ₪{vacation.vacation_price.toLocaleString()}
                            </Typography>
                            <Typography sx={{ marginBottom: 2 }}>
                                <strong>תיאור מפורט:</strong> {vacation.vacation_description}
                            </Typography>
                            <Typography>
                                חופשה נהדרת ב{vacation.country_name}! הזמן המושלם לנוח ולהנות מהנוף המדהים.
                                המחיר כולל לינה, ארוחות ופעילויות מגוונות.
                            </Typography>
                        </CardContent>
                    </Collapse>
                </Card>
            ))}
        </div>
    );
}