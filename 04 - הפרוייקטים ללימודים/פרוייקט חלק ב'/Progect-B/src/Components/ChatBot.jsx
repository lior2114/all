import React, { useState, useRef, useEffect } from 'react';
import {
    Box,
    Paper,
    Typography,
    TextField,
    IconButton,
    Avatar,
    Fab,
    Slide,
    Fade,
    CircularProgress,
    Chip,
    Tooltip,
    Link
} from '@mui/material';
import {
    Chat as ChatIcon,
    Send as SendIcon,
    Close as CloseIcon,
    SmartToy as BotIcon,
    Person as PersonIcon,
    RestartAlt as RestartIcon,
    Minimize as MinimizeIcon
} from '@mui/icons-material';
import { useChat } from '../Contexts/ChatContext';
import { useUi } from '../Contexts/UiContext';
import { useNavigate, useLocation } from 'react-router-dom';

export function ChatBot() {
    const { 
        isOpen, 
        messages, 
        isTyping, 
        toggleChat, 
        processUserMessage, 
        clearChat 
    } = useChat();
    const { language, mode } = useUi();
    const navigate = useNavigate();
    const location = useLocation();
    const [inputValue, setInputValue] = useState('');
    const [isMinimized, setIsMinimized] = useState(false);
    const [hasClosedOnHomePage, setHasClosedOnHomePage] = useState(false);
    const messagesEndRef = useRef(null);
    const inputRef = useRef(null);
    const previousPathRef = useRef(location.pathname);

    const t = (he, en) => (language === 'he' ? he : en);

    // פונקציה לטיפול בסגירת הצ'אט
    const handleToggleChat = () => {
        if (isOpen && location.pathname === '/') {
            // אם סוגרים את הצ'אט בדף הבית - תזכור את זה
            setHasClosedOnHomePage(true);
        }
        toggleChat();
    };

    // בדיקה אם חזר לדף הבית מעמוד אחר
    useEffect(() => {
        if (previousPathRef.current !== '/' && location.pathname === '/') {
            // חזר לדף הבית מעמוד אחר - אפס את הדגל
            setHasClosedOnHomePage(false);
        }
        previousPathRef.current = location.pathname;
    }, [location.pathname]);

    // פתיחת הצ'אט אוטומטית בדף הבית
    useEffect(() => {
        if (location.pathname === '/' && !isOpen && !hasClosedOnHomePage) {
            setTimeout(() => {
                toggleChat();
            }, 500);
        }
    }, [location.pathname, isOpen, hasClosedOnHomePage, toggleChat]);

    // גלילה אוטומטית לתחתית
    useEffect(() => {
        if (messagesEndRef.current) {
            messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
        }
    }, [messages, isTyping]);

    // מיקוד על שדה הקלט כשהצ'אט נפתח
    useEffect(() => {
        if (isOpen && !isMinimized && inputRef.current) {
            setTimeout(() => inputRef.current?.focus(), 300);
        }
    }, [isOpen, isMinimized]);

    const handleSendMessage = async () => {
        const message = inputValue.trim();
        if (!message) return;

        setInputValue('');
        await processUserMessage(message);
    };

    const handleKeyPress = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    const formatMessageContent = (content) => {
        // המרת טקסט לפורמט עם line breaks ו-styling
        return content.split('\n').map((line, index) => {
            // זיהוי כותרות (מתחילות ב-**)
            if (line.startsWith('**') && line.endsWith('**')) {
                return (
                    <Typography 
                        key={index} 
                        variant="subtitle2" 
                        sx={{ fontWeight: 'bold', color: 'primary.main', my: 0.5 }}
                    >
                        {line.slice(2, -2)}
                    </Typography>
                );
            }
            
            // זיהוי קישורים [טקסט](/path)
            const linkRegex = /\[([^\]]+)\]\(([^\)]+)\)/g;
            if (linkRegex.test(line)) {
                const parts = [];
                let lastIndex = 0;
                let match;
                const regex = /\[([^\]]+)\]\(([^\)]+)\)/g;
                
                while ((match = regex.exec(line)) !== null) {
                    // הוסף טקסט לפני הקישור
                    if (match.index > lastIndex) {
                        parts.push(line.substring(lastIndex, match.index));
                    }
                    
                    // הוסף את הקישור
                    parts.push(
                        <Link
                            key={`link-${index}-${match.index}`}
                            component="button"
                            variant="body2"
                            onClick={() => {
                                navigate(match[2]);
                                toggleChat(); // סגור את הצ'אט אחרי הניווט
                            }}
                            sx={{
                                color: 'primary.main',
                                textDecoration: 'underline',
                                cursor: 'pointer',
                                '&:hover': {
                                    color: 'primary.dark',
                                }
                            }}
                        >
                            {match[1]}
                        </Link>
                    );
                    
                    lastIndex = match.index + match[0].length;
                }
                
                // הוסף טקסט אחרי הקישור האחרון
                if (lastIndex < line.length) {
                    parts.push(line.substring(lastIndex));
                }
                
                return (
                    <Typography key={index} variant="body2" sx={{ my: 0.25 }}>
                        {parts}
                    </Typography>
                );
            }
            
            // זיהוי רשימות (מתחילות עם •)
            if (line.trim().startsWith('•')) {
                return (
                    <Typography 
                        key={index} 
                        variant="body2" 
                        sx={{ ml: 1, my: 0.25 }}
                    >
                        {line}
                    </Typography>
                );
            }
            
            // זיהוי מספור (מתחיל עם מספר.)
            if (/^\d+\./.test(line.trim())) {
                return (
                    <Typography 
                        key={index} 
                        variant="body2" 
                        sx={{ fontWeight: 'medium', my: 0.5 }}
                    >
                        {line}
                    </Typography>
                );
            }
            
            // טקסט רגיל
            if (line.trim()) {
                return (
                    <Typography key={index} variant="body2" sx={{ my: 0.25 }}>
                        {line}
                    </Typography>
                );
            }
            
            // שורה ריקה
            return <Box key={index} sx={{ height: 8 }} />;
        });
    };

    const quickSuggestions = [
        '/cheap',
        t('חופשות באירופה', 'European vacations'),
        t('עד 5000 שקל', 'Under 5000 NIS'),
        t('10 דולר', '10 dollars'),
        '/currencies',
        '/soon',
        '/help'
    ];

    const handleSuggestionClick = (suggestion) => {
        setInputValue(suggestion);
        // שליחה אוטומטית של ההצעה
        setTimeout(() => {
            processUserMessage(suggestion);
        }, 100);
    };

    // כפתור צף
    if (!isOpen) {
        return (
            <Tooltip title={t('צ\'אט עזרה חכם', 'Smart Help Chat')} placement="top">
                <Fab
                    color="primary"
                    sx={{
                        position: 'fixed',
                        bottom: 24,
                        right: 24,
                        zIndex: 1000,
                        background: 'linear-gradient(45deg, #2196F3 30%, #21CBF3 90%)',
                        '&:hover': {
                            background: 'linear-gradient(45deg, #1976D2 30%, #1EAEDB 90%)',
                            transform: 'scale(1.1)',
                        },
                        transition: 'all 0.3s ease',
                        boxShadow: '0 4px 20px rgba(33, 150, 243, 0.4)',
                    }}
                    onClick={toggleChat}
                >
                    <ChatIcon />
                </Fab>
            </Tooltip>
        );
    }

    return (
        <Slide direction="up" in={isOpen} timeout={300}>
            <Paper
                elevation={8}
                sx={{
                    position: 'fixed',
                    bottom: 24,
                    right: 24,
                    width: { xs: 'calc(100vw - 48px)', sm: 400 },
                    height: isMinimized ? 'auto' : { xs: 'calc(100vh - 100px)', sm: 600 },
                    zIndex: 1000,
                    borderRadius: 3,
                    overflow: 'hidden',
                    background: mode === 'dark' 
                        ? 'linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%)'
                        : 'linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%)',
                    border: mode === 'dark' ? '1px solid #333' : '1px solid #e0e0e0',
                    display: 'flex',
                    flexDirection: 'column',
                    transition: 'all 0.3s ease',
                }}
            >
                {/* כותרת הצ'אט */}
                <Box
                    sx={{
                        p: 2,
                        background: 'linear-gradient(45deg, #2196F3 30%, #21CBF3 90%)',
                        color: 'white',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'space-between',
                    }}
                >
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <Avatar sx={{ bgcolor: 'rgba(255,255,255,0.2)', width: 32, height: 32 }}>
                            <BotIcon fontSize="small" />
                        </Avatar>
                        <Box>
                            <Typography variant="subtitle1" sx={{ fontWeight: 'bold', lineHeight: 1.2 }}>
                                {t('עוזר החופשות החכם', 'Smart Vacation Assistant')}
                            </Typography>
                            <Typography variant="caption" sx={{ opacity: 0.8 }}>
                                {isTyping ? t('מקליד...', 'Typing...') : t('זמין לעזרה', 'Ready to help')}
                            </Typography>
                        </Box>
                    </Box>
                    <Box>
                        <Tooltip title={t("מזעור הצ'אט", "Minimize Chat")}>
                            <IconButton 
                                size="small" 
                                sx={{ color: 'white', mr: 1 }} 
                                onClick={() => setIsMinimized(!isMinimized)}
                            >
                                <MinimizeIcon fontSize="small" />
                            </IconButton>
                        </Tooltip>
                        <Tooltip title={t("איפוס הצ'אט", "Reset Chat")}>
                            <IconButton 
                                size="small" 
                                sx={{ color: 'white', mr: 1 }} 
                                onClick={clearChat}
                            >
                                <RestartIcon fontSize="small" />
                            </IconButton>
                        </Tooltip>
                        <Tooltip title={t("סגירת הצ'אט", "Close Chat")}>
                            <IconButton size="small" sx={{ color: 'white' }} onClick={handleToggleChat}>
                                <CloseIcon fontSize="small" />
                            </IconButton>
                        </Tooltip>
                    </Box>
                </Box>

                {!isMinimized && (
                    <>
                        {/* אזור הודעות */}
                        <Box
                            sx={{
                                flex: 1,
                                overflowY: 'auto',
                                p: 2,
                                display: 'flex',
                                flexDirection: 'column',
                                gap: 2,
                                '&::-webkit-scrollbar': {
                                    width: '6px',
                                },
                                '&::-webkit-scrollbar-track': {
                                    background: 'transparent',
                                },
                                '&::-webkit-scrollbar-thumb': {
                                    background: mode === 'dark' ? '#555' : '#ddd',
                                    borderRadius: '3px',
                                },
                            }}
                        >
                            {messages.map((message) => (
                                <Fade key={message.id} in timeout={300}>
                                    <Box
                                        sx={{
                                            display: 'flex',
                                            justifyContent: message.type === 'user' ? 'flex-end' : 'flex-start',
                                            alignItems: 'flex-start',
                                            gap: 1,
                                        }}
                                    >
                                        {message.type === 'bot' && (
                                            <Avatar 
                                                sx={{ 
                                                    bgcolor: 'primary.main', 
                                                    width: 32, 
                                                    height: 32,
                                                    mt: 0.5
                                                }}
                                            >
                                                <BotIcon fontSize="small" />
                                            </Avatar>
                                        )}
                                        
                                        <Paper
                                            elevation={1}
                                            sx={{
                                                p: 2,
                                                maxWidth: '75%',
                                                backgroundColor: 
                                                    message.type === 'user' 
                                                        ? 'primary.main'
                                                        : mode === 'dark' ? '#333' : '#f5f5f5',
                                                color: 
                                                    message.type === 'user' 
                                                        ? 'white'
                                                        : 'text.primary',
                                                borderRadius: 
                                                    message.type === 'user'
                                                        ? '20px 20px 5px 20px'
                                                        : '20px 20px 20px 5px',
                                                wordBreak: 'break-word',
                                            }}
                                        >
                                            {message.type === 'user' ? (
                                                <Typography variant="body2">
                                                    {message.content}
                                                </Typography>
                                            ) : (
                                                <Box>
                                                    {formatMessageContent(message.content)}
                                                </Box>
                                            )}
                                            
                                            <Typography 
                                                variant="caption" 
                                                sx={{ 
                                                    opacity: 0.7, 
                                                    display: 'block', 
                                                    textAlign: message.type === 'user' ? 'right' : 'left',
                                                    mt: 1
                                                }}
                                            >
                                                {new Date(message.timestamp).toLocaleTimeString('he-IL', {
                                                    hour: '2-digit',
                                                    minute: '2-digit'
                                                })}
                                            </Typography>
                                        </Paper>

                                        {message.type === 'user' && (
                                            <Avatar 
                                                sx={{ 
                                                    bgcolor: 'secondary.main', 
                                                    width: 32, 
                                                    height: 32,
                                                    mt: 0.5
                                                }}
                                            >
                                                <PersonIcon fontSize="small" />
                                            </Avatar>
                                        )}
                                    </Box>
                                </Fade>
                            ))}

                            {/* אינדיקטור הקלדה */}
                            {isTyping && (
                                <Fade in timeout={300}>
                                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                        <Avatar 
                                            sx={{ 
                                                bgcolor: 'primary.main', 
                                                width: 32, 
                                                height: 32
                                            }}
                                        >
                                            <BotIcon fontSize="small" />
                                        </Avatar>
                                        <Paper
                                            elevation={1}
                                            sx={{
                                                p: 2,
                                                backgroundColor: mode === 'dark' ? '#333' : '#f5f5f5',
                                                borderRadius: '20px 20px 20px 5px',
                                                display: 'flex',
                                                alignItems: 'center',
                                                gap: 1,
                                            }}
                                        >
                                            <CircularProgress size={16} />
                                            <Typography variant="body2" color="text.secondary">
                                                {t('מכין תשובה...', 'Preparing response...')}
                                            </Typography>
                                        </Paper>
                                    </Box>
                                </Fade>
                            )}

                            <div ref={messagesEndRef} />
                        </Box>

                        {/* הצעות מהירות */}
                        {messages.length <= 2 && (
                            <Box sx={{ px: 2, pb: 1 }}>
                                <Typography variant="caption" color="text.secondary" sx={{ mb: 1, display: 'block' }}>
                                    {t('או בחר נושא:', 'Or choose a topic:')}
                                </Typography>
                                <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                                    {quickSuggestions.map((suggestion, index) => (
                                        <Chip
                                            key={`${suggestion}-${index}`} // עדכן key כדי לעקוב אחרי שינויי שפה
                                            label={suggestion}
                                            size="small"
                                            variant="outlined"
                                            onClick={() => handleSuggestionClick(suggestion)}
                                            sx={{ 
                                                cursor: 'pointer',
                                                '&:hover': {
                                                    backgroundColor: 'primary.light',
                                                    color: 'white',
                                                }
                                            }}
                                        />
                                    ))}
                                </Box>
                            </Box>
                        )}

                        {/* שדה קלט */}
                        <Box
                            sx={{
                                p: 2,
                                borderTop: `1px solid ${mode === 'dark' ? '#333' : '#e0e0e0'}`,
                                backgroundColor: mode === 'dark' ? '#1e1e1e' : '#fafafa',
                            }}
                        >
                            <Box sx={{ display: 'flex', gap: 1, alignItems: 'flex-end' }}>
                                <TextField
                                    ref={inputRef}
                                    fullWidth
                                    variant="outlined"
                                    placeholder={t('כתוב הודעה...', 'Type a message...')}
                                    value={inputValue}
                                    onChange={(e) => setInputValue(e.target.value)}
                                    onKeyPress={handleKeyPress}
                                    disabled={isTyping}
                                    multiline
                                    maxRows={3}
                                    sx={{
                                        '& .MuiOutlinedInput-root': {
                                            borderRadius: '25px',
                                            backgroundColor: mode === 'dark' ? '#2d2d2d' : 'white',
                                        },
                                    }}
                                />
                                <IconButton
                                    color="primary"
                                    onClick={handleSendMessage}
                                    disabled={!inputValue.trim() || isTyping}
                                    sx={{
                                        backgroundColor: 'primary.main',
                                        color: 'white',
                                        '&:hover': {
                                            backgroundColor: 'primary.dark',
                                        },
                                        '&:disabled': {
                                            backgroundColor: 'action.disabled',
                                        }
                                    }}
                                >
                                    <SendIcon />
                                </IconButton>
                            </Box>
                        </Box>
                    </>
                )}
            </Paper>
        </Slide>
    );
}
