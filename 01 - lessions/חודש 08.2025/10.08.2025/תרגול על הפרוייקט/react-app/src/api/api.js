const API_URL = "http://localhost:5000";

export const register = async (userData) => {
    try {
        const response = await fetch(`${API_URL}/users`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData)
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.Error || 'Registration failed');
        }
        
        return response.json();
    } catch (error) {
        console.error('Registration error:', error);
        throw error;
    }
}

export const login = async (userData) => {
    try {
        const response = await fetch(`${API_URL}/users/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(userData)
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.Error || 'שגיאה בהתחברות');
        }
        
        return response.json();
    } catch (error) {
        console.error('Login error:', error);
        throw error;
    }
}

// פונקציה לקבלת כל החופשות
export const getVacations = async () => {
    try {
        const response = await fetch(`${API_URL}/vacations`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        });
        
        if (!response.ok) {
            throw new Error('Failed to fetch vacations');
        }
        
        return response.json();
    } catch (error) {
        console.error('Get vacations error:', error);
        throw error;
    }
}

// פונקציה לקבלת כל הלייקים
export const getLikes = async () => {
    try {
        const response = await fetch(`${API_URL}/likes`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        });
        
        if (!response.ok) {
            throw new Error('Failed to fetch likes');
        }
        
        return response.json();
    } catch (error) {
        console.error('Get likes error:', error);
        throw error;
    }
}

// פונקציה להוספת לייק
export const addLike = async (userId, vacationId) => {
    try {
        const response = await fetch(`${API_URL}/likes`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                user_id: userId,
                vacation_id: vacationId
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to add like');
        }
        
        return response.json();
    } catch (error) {
        console.error('Add like error:', error);
        throw error;
    }
}

// פונקציה להסרת לייק
export const removeLike = async (userId, vacationId) => {
    try {
        const response = await fetch(`${API_URL}/likes`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                user_id: userId,
                vacation_id: vacationId
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to remove like');
        }
        
        return response.json();
    } catch (error) {
        console.error('Remove like error:', error);
        throw error;
    }
}

// פונקציה לקבלת תמונות לפי מדינה
export const getVacationImage = (countryName) => {
    // בדיקה אם countryName קיים
    if (!countryName) {
        return 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=400&h=300&fit=crop';
    }
    
    const imageMap = {
        'france': 'https://images.unsplash.com/photo-1502602898536-47ad22581b52?w=400&h=300&fit=crop',
        'england': 'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=400&h=300&fit=crop',
        'usa': 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=400&h=300&fit=crop',
        'japan': 'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=400&h=300&fit=crop',
        'italy': 'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=400&h=300&fit=crop',
        'spain': 'https://images.unsplash.com/photo-1539037116277-4db20889f2d4?w=400&h=300&fit=crop',
        'netherlands': 'https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?w=400&h=300&fit=crop',
        'czech republic': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'austria': 'https://images.unsplash.com/photo-1516550893923-42d28e5677af?w=400&h=300&fit=crop',
        'hungary': 'https://images.unsplash.com/photo-1551867633-194f125695d7?w=400&h=300&fit=crop',
        'greece': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'turkey': 'https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?w=400&h=300&fit=crop',
        'russia': 'https://images.unsplash.com/photo-1513326738677-b964603b136d?w=400&h=300&fit=crop',
        'china': 'https://images.unsplash.com/photo-1508804185872-d7badad00f7d?w=400&h=300&fit=crop',
        'south korea': 'https://images.unsplash.com/photo-1538485399081-7c8ce013b933?w=400&h=300&fit=crop',
        'india': 'https://images.unsplash.com/photo-1570168007204d1a1c6e2b9b8?w=400&h=300&fit=crop',
        'brazil': 'https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=400&h=300&fit=crop',
        'australia': 'https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=400&h=300&fit=crop',
        'egypt': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop',
        'thailand': 'https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?w=400&h=300&fit=crop',
        'israel': 'https://images.unsplash.com/photo-1548013146-72479768bada?w=400&h=300&fit=crop',
        'germany': 'https://images.unsplash.com/photo-1526772662000-3f88f10405ff?w=400&h=300&fit=crop',
        'switzerland': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'portugal': 'https://images.unsplash.com/photo-1555881400-74d7acaacd8b?w=400&h=300&fit=crop',
        'ireland': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'scotland': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'wales': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'norway': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'sweden': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'denmark': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'finland': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400&h=300&fit=crop',
        'poland': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'ukraine': 'https://images.unsplash.com/photo-1513326738677-b964603b136d?w=400&h=300&fit=crop',
        'belarus': 'https://images.unsplash.com/photo-1513326738677-b964603b136d?w=400&h=300&fit=crop',
        'lithuania': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'latvia': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'estonia': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'slovakia': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'slovenia': 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=400&h=300&fit=crop',
        'croatia': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'serbia': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'bulgaria': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'romania': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'moldova': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'albania': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'macedonia': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'montenegro': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'bosnia': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop',
        'kosovo': 'https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?w=400&h=300&fit=crop'
    };
    
    const countryLower = countryName.toLowerCase();
    
    // חיפוש מדויק
    if (imageMap[countryLower]) {
        return imageMap[countryLower];
    }
    
    // חיפוש חלקי
    for (const [key, imageUrl] of Object.entries(imageMap)) {
        if (countryLower.includes(key) || key.includes(countryLower)) {
            return imageUrl;
        }
    }
    
    // אם לא נמצא, החזר תמונת ברירת מחדל
    return 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=400&h=300&fit=crop';
}

// פונקציה לקבלת החופשות האהובות של משתמש
export const getUserFavoriteVacations = async (userId) => {
    try {
        const [likesData, vacationsData] = await Promise.all([
            getLikes(),
            getVacations()
        ]);
        
        // מציאת החופשות שהמשתמש עשה להן לייק
        const userLikes = likesData.filter(like => like[0] === userId);
        const favoriteVacationIds = userLikes.map(like => like[1]);
        
        // סינון החופשות האהובות
        const favoriteVacations = vacationsData.filter(vacation => 
            favoriteVacationIds.includes(vacation.vacation_id)
        );
        
        return favoriteVacations;
    } catch (error) {
        console.error('Error getting user favorite vacations:', error);
        throw error;
    }
}



// פונקציה לעדכון פרטי משתמש
export const updateUser = async (userId, userData) => {
    try {
        const response = await fetch(`http://localhost:5000/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        });

        if (!response.ok) {
            let errorMessage = 'שגיאה בעדכון המשתמש';
            try {
                const errorData = await response.json();
                errorMessage = errorData.Error || errorData.error || errorMessage;
            } catch (parseError) {
                console.error('Error parsing response:', parseError);
                const textResponse = await response.text();
                console.error('Response text:', textResponse);
            }
            throw new Error(errorMessage);
        }

        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error updating user:', error);
        throw error;
    }
}

// פונקציות לניהול אדמין

// הוספת חופשה חדשה
export const addVacation = async (vacationData) => {
    try {
        console.log('Sending vacation data:', vacationData);
        const response = await fetch(`${API_URL}/vacations`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(vacationData)
        });

        console.log('Response status:', response.status);
        console.log('Response headers:', response.headers);
        
        if (!response.ok) {
            let errorMessage = 'שגיאה בהוספת החופשה';
            try {
                const errorData = await response.json();
                console.log('Error data:', errorData);
                errorMessage = errorData.Error || errorData.error || errorMessage;
            } catch (parseError) {
                console.error('Error parsing response:', parseError);
                // אם לא מצליח לפרסר JSON, ננסה לקרוא כטקסט
                const textResponse = await response.text();
                console.error('Response text:', textResponse);
            }
            throw new Error(errorMessage);
        }

        return await response.json();
    } catch (error) {
        console.error('Error adding vacation:', error);
        throw error;
    }
};

// מחיקת חופשה
export const deleteVacation = async (vacationId) => {
    try {
        const response = await fetch(`${API_URL}/vacations/${vacationId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'שגיאה במחיקת החופשה');
        }

        return await response.json();
    } catch (error) {
        console.error('Error deleting vacation:', error);
        throw error;
    }
};

// קבלת כל המשתמשים
export const getAllUsers = async () => {
    try {
        const response = await fetch(`${API_URL}/users`);
        
        if (!response.ok) {
            throw new Error('Failed to fetch users');
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error fetching users:', error);
        throw error;
    }
};

// עדכון משתמש (על ידי אדמין)
export const updateUserByAdmin = async (userId, userData) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'שגיאה בעדכון המשתמש');
        }

        return await response.json();
    } catch (error) {
        console.error('Error updating user:', error);
        throw error;
    }
};

// מחיקת משתמש
export const deleteUser = async (userId) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}`, {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.Error || errorData.error || 'שגיאה במחיקת המשתמש');
        }

        return await response.json();
    } catch (error) {
        console.error('Error deleting user:', error);
        throw error;
    }
};

// עדכון חופשה
export const updateVacation = async (vacationId, vacationData) => {
    try {
        const response = await fetch(`${API_URL}/vacations/update/${vacationId}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(vacationData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.Error || errorData.error || 'שגיאה בעדכון החופשה');
        }

        return await response.json();
    } catch (error) {
        console.error('Error updating vacation:', error);
        throw error;
    }
};

// העלאת תמונה לחופשה
export const uploadVacationImage = async (file) => {
    try {
        const formData = new FormData();
        formData.append('image', file);

        const response = await fetch(`${API_URL}/vacations/upload-image`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.Error || errorData.error || 'שגיאה בהעלאת התמונה');
        }

        return await response.json();
    } catch (error) {
        console.error('Error uploading image:', error);
        throw error;
    }
};

// קבלת URL של תמונת חופשה
export const getVacationImageUrl = (filename) => {
    if (!filename) {
        return 'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=400&h=300&fit=crop';
    }
    return `${API_URL}/uploads/${filename}`;
};

// קבלת כל המדינות
export const getCountries = async () => {
    try {
        const response = await fetch(`${API_URL}/countries`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
            }
        });
        
        if (!response.ok) {
            throw new Error('Failed to fetch countries');
        }
        
        return response.json();
    } catch (error) {
        console.error('Get countries error:', error);
        throw error;
    }
};

// הרחקת משתמש
export const banUser = async (userId, banData) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}/ban`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(banData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'שגיאה בהרחקת המשתמש');
        }

        return await response.json();
    } catch (error) {
        console.error('Error banning user:', error);
        throw error;
    }
};

// ביטול הרחקת משתמש
export const unbanUser = async (userId) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}/unban`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'שגיאה בביטול הרחקת המשתמש');
        }

        return await response.json();
    } catch (error) {
        console.error('Error unbanning user:', error);
        throw error;
    }
};

// עדכון תמונת פרופיל
export const updateProfileImage = async (userId, formData) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}/profile-image`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'שגיאה בעדכון תמונת הפרופיל');
        }

        return await response.json();
    } catch (error) {
        console.error('Error updating profile image:', error);
        throw error;
    }
};

// הסרת תמונת פרופיל
export const removeProfileImage = async (userId) => {
    try {
        const response = await fetch(`${API_URL}/users/${userId}/profile-image`, {
            method: 'DELETE'
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'שגיאה בהסרת תמונת הפרופיל');
        }

        return await response.json();
    } catch (error) {
        console.error('Error removing profile image:', error);
        throw error;
    }
};
