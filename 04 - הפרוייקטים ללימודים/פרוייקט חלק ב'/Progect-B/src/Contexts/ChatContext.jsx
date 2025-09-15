import React, { createContext, useContext, useState, useEffect } from 'react';
import { getVacations } from '../api/api';
import { useUi } from './UiContext';

const ChatContext = createContext();

export const useChat = () => {
    const context = useContext(ChatContext);
    if (!context) {
        throw new Error('useChat must be used within ChatProvider');
    }
    return context;
};

export const ChatProvider = ({ children }) => {
    const { language } = useUi();
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState(() => {
        try {
            const saved = localStorage.getItem('chatHistory');
            return saved ? JSON.parse(saved) : [];
        } catch {
            return [];
        }
    });
    const [isTyping, setIsTyping] = useState(false);
    const [vacations, setVacations] = useState([]);

    // פונקציית תרגום
    const t = (he, en) => (language === 'he' ? he : en);

    // הוסף הודעת ברכה אם אין הודעות
    useEffect(() => {
        // יצירת הודעת ברכה דינמית לפי שפה
        const getWelcomeMessage = () => ({
            id: Date.now(),
            type: 'bot',
            content: t(
                'שלום! אני כאן כדי לעזור לך למצוא את החופשה המושלמת 🏖️\n\nאני יכול לעזור לך עם:\n• חיפוש חופשות לפי תאריכים\n• מיון לפי טווח מחירים\n• חיפוש לפי יעד או אזור\n• המלצות מותאמות אישית\n\nמה תרצה לדעת?',
                'Hello! I\'m here to help you find the perfect vacation 🏖️\n\nI can help you with:\n• Search vacations by dates\n• Sort by price range\n• Search by destination or area\n• Personalized recommendations\n\nWhat would you like to know?'
            ),
            timestamp: new Date()
        });

        if (messages.length === 0) {
            setMessages([getWelcomeMessage()]);
        }
    }, [language, messages.length, t]); // עדכן כאשר השפה משתנה או כשאין הודעות

    // טען רשימת חופשות בהתחלה
    useEffect(() => {
        const loadVacations = async () => {
            try {
                const data = await getVacations();
                setVacations(Array.isArray(data) ? data : []);
            } catch (error) {
                console.error('Failed to load vacations for chat:', error);
            }
        };
        loadVacations();
    }, []);

    // שמור היסטוריית צ'אט
    useEffect(() => {
        try {
            localStorage.setItem('chatHistory', JSON.stringify(messages));
        } catch (error) {
            console.error('Failed to save chat history:', error);
        }
    }, [messages]);

    const addMessage = (content, type = 'user') => {
        const newMessage = {
            id: Date.now() + Math.random(),
            type,
            content,
            timestamp: new Date()
        };
        setMessages(prev => [...prev, newMessage]);
        return newMessage;
    };

    const processUserMessage = async (userInput) => {
        // הוסף הודעת המשתמש
        addMessage(userInput, 'user');
        
        setIsTyping(true);
        
        // המתן קצר לאפקט הקלדה
        setTimeout(async () => {
            const response = await generateAIResponse(userInput);
            addMessage(response, 'bot');
            setIsTyping(false);
        }, 1000 + Math.random() * 1000);
    };

    const generateAIResponse = async (input) => {
        const lowerInput = input.toLowerCase();
        
        // פקודות מיוחדות
        if (input.startsWith('/')) {
            return handleSpecialCommands(input);
        }
        
        // זיהוי כוונות משתמש
        if (containsDateQuery(lowerInput)) {
            return handleDateQuery(input, lowerInput);
        }
        
        if (containsPriceQuery(lowerInput)) {
            return handlePriceQuery(input, lowerInput);
        }
        
        if (containsLocationQuery(lowerInput)) {
            return handleLocationQuery(input, lowerInput);
        }
        
        if (containsGeneralVacationQuery(lowerInput)) {
            return handleGeneralVacationQuery(input, lowerInput);
        }
        
        if (containsGreeting(lowerInput)) {
            return handleGreeting();
        }
        
        // תשובה כללית
        return handleGeneralQuery(input);
    };

    // פונקציות זיהוי כוונות
    const containsDateQuery = (input) => {
        const dateKeywords = ['תאריך', 'תאריכים', 'חודש', 'יום', 'שבוע', 'מתי', 'זמן', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר', 'ינואר'];
        return dateKeywords.some(keyword => input.includes(keyword)) || /\d{1,2}\/\d{1,2}/.test(input) || /\d{4}-\d{2}-\d{2}/.test(input);
    };

    const containsPriceQuery = (input) => {
        const priceKeywords = ['מחיר', 'עלות', 'כסף', 'שקל', 'זול', 'יקר', 'תקציב', 'עד', 'מ-', 'בין', 'dollar', '$', '₪', 'דולר', 'יורו', 'euro', '€', 'פאונד', 'pound', '£', 'nis'];
        return priceKeywords.some(keyword => input.includes(keyword)) || /\d+\s*(דולר|יורו|שקל|dollar|euro|pound|פאונד|\$|€|£|₪)/.test(input);
    };

    const containsLocationQuery = (input) => {
        const locationKeywords = ['מדינה', 'יעד', 'איפה', 'אזור', 'מקום', 'עיר', 'כפר', 'ים', 'הרים', 'מדבר', 'כפרי', 'עירוני', 'חוף', 'אירופה', 'אסיה', 'אמריקה'];
        const countries = ['israel', 'italy', 'france', 'spain', 'greece', 'turkey', 'egypt', 'thailand', 'japan', 'usa', 'germany', 'netherlands', 'ישראל', 'איטליה', 'צרפת', 'ספרד', 'יוון', 'טורקיה', 'מצרים', 'תאילנד', 'יפן', 'ארהב', 'גרמניה', 'הולנד'];
        return locationKeywords.some(keyword => input.includes(keyword)) || 
               countries.some(country => input.includes(country));
    };

    const containsGeneralVacationQuery = (input) => {
        const vacationKeywords = ['חופשה', 'חופשות', 'טיול', 'טיולים', 'נסיעה', 'נופש', 'חופש', 'בריחה', 'מזג אוויר', 'פעילויות'];
        return vacationKeywords.some(keyword => input.includes(keyword));
    };

    const containsGreeting = (input) => {
        const greetings = ['שלום', 'היי', 'הי', 'אהלן', 'ברוך הבא', 'טוב', 'מה קורה', 'מה נשמע'];
        return greetings.some(greeting => input.includes(greeting));
    };

    // פונקציה לטיפול בפקודות מיוחדות
    const handleSpecialCommands = (input) => {
        const command = input.toLowerCase().trim();
        
        switch (command) {
            case '/help':
            case '/עזרה':
                return t(
                    `🤖 **פקודות זמינות:**\n\n` +
                    `**חיפוש חופשות:**\n` +
                    `• כתוב תאריך (לדוגמה: "15/7/2024")\n` +
                    `• כתוב תקציב (לדוגמה: "עד 5000 שקל", "2 דולר")\n` +
                    `• כתוב יעד (לדוגמה: "חופשה באיטליה")\n\n` +
                    `**פקודות מיוחדות:**\n` +
                    `• /help - רשימת פקודות\n` +
                    `• /vacations - קישור לכל החופשות\n` +
                    `• /cheap - החופשות הזולות ביותר\n` +
                    `• /expensive - החופשות היקרות ביותר\n` +
                    `• /soon - החופשות הקרובות ביותר\n` +
                    `• /currencies - פילוח לפי מטבעות\n` +
                    `• /clear - ניקוי צ'אט\n\n` +
                    `💱 **מטבעות נתמכים:** שקל, דולר, יורו, פאונד\n` +
                    `💡 תוכל פשוט לכתוב באופן טבעי מה שאתה מחפש!`,
                    
                    `🤖 **Available Commands:**\n\n` +
                    `**Search Vacations:**\n` +
                    `• Write a date (e.g., "15/7/2024")\n` +
                    `• Write a budget (e.g., "up to 5000 shekels", "2 dollars")\n` +
                    `• Write a destination (e.g., "vacation in Italy")\n\n` +
                    `**Special Commands:**\n` +
                    `• /help - command list\n` +
                    `• /vacations - link to all vacations\n` +
                    `• /cheap - cheapest vacations\n` +
                    `• /expensive - most expensive vacations\n` +
                    `• /soon - upcoming vacations\n` +
                    `• /currencies - breakdown by currencies\n` +
                    `• /clear - clear chat\n\n` +
                    `💱 **Supported currencies:** Shekel, Dollar, Euro, Pound\n` +
                    `💡 You can simply write naturally what you're looking for!`
                );
                       
            case '/vacations':
            case '/חופשות':
                return t(
                    `🏖️ **כל החופשות שלנו זמינות כאן:**\n\n` +
                    `🔗 [צפייה בכל החופשות](/vacations)\n\n` +
                    `יש לנו ${vacations.length} חופשות מדהימות שמחכות לך!\n` +
                    `תוכל למיין לפי מחיר, תאריך או יעד.`,
                    
                    `🏖️ **All our vacations are available here:**\n\n` +
                    `🔗 [View all vacations](/vacations)\n\n` +
                    `We have ${vacations.length} amazing vacations waiting for you!\n` +
                    `You can sort by price, date or destination.`
                );
                       
            case '/cheap':
            case '/זול':
                const cheapVacations = vacations
                    .filter(v => v.vacation_price < 4000)
                    .sort((a, b) => a.vacation_price - b.vacation_price)
                    .slice(0, 3);
                if (cheapVacations.length === 0) {
                    return t(
                        `לא נמצאו חופשות תחת 4,000 ₪ 😔\nאבל יש לנו אפשרויות נהדרות בכל הטווחים!`,
                        `No vacations found under 4,000 ₪ 😔\nBut we have great options in all price ranges!`
                    );
                }
                let cheapResponse = t(
                    `💰 **החופשות הזולות ביותר:**\n\n`,
                    `💰 **Cheapest Vacations:**\n\n`
                );
                cheapVacations.forEach((vacation, index) => {
                    cheapResponse += `${index + 1}. **${vacation.country_name}**\n`;
                    cheapResponse += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n`;
                    cheapResponse += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n\n`;
                });
                return cheapResponse;
                
            case '/expensive':
            case '/יקר':
                const expensiveVacations = vacations
                    .filter(v => v.vacation_price > 6000)
                    .sort((a, b) => b.vacation_price - a.vacation_price)
                    .slice(0, 3);
                if (expensiveVacations.length === 0) {
                    return `לא נמצאו חופשות מעל 6,000 ₪ 🤔\nאבל יש לנו אפשרויות מדהימות בכל הטווחים!`;
                }
                let expensiveResponse = `💎 **החופשות הפרימיום:**\n\n`;
                expensiveVacations.forEach((vacation, index) => {
                    expensiveResponse += `${index + 1}. **${vacation.country_name}**\n`;
                    expensiveResponse += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n`;
                    expensiveResponse += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n\n`;
                });
                return expensiveResponse;
                
            case '/soon':
            case '/קרוב':
                const soonVacations = vacations
                    .filter(v => new Date(v.vacation_start) > new Date())
                    .sort((a, b) => new Date(a.vacation_start) - new Date(b.vacation_start))
                    .slice(0, 3);
                if (soonVacations.length === 0) {
                    return `לא נמצאו חופשות קרובות 😔\nאולי כדאי לבדוק תאריכים אחרים!`;
                }
                let soonResponse = `⏰ **החופשות הקרובות ביותר:**\n\n`;
                soonVacations.forEach((vacation, index) => {
                    soonResponse += `${index + 1}. **${vacation.country_name}**\n`;
                    soonResponse += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n`;
                    soonResponse += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n\n`;
                });
                return soonResponse;
                
            case '/clear':
            case '/נקה':
                setTimeout(() => clearChat(), 500);
                return `🧹 הצ'אט ינוקה בעוד רגע...`;
                
            case '/currencies':
            case '/מטבעות':
                const currencyBreakdown = {};
                vacations.forEach(v => {
                    const currency = v.vacation_currency || 'ILS';
                    if (!currencyBreakdown[currency]) {
                        currencyBreakdown[currency] = { count: 0, prices: [] };
                    }
                    currencyBreakdown[currency].count++;
                    currencyBreakdown[currency].prices.push(v.vacation_price);
                });
                
                let currencyResponse = `💱 **החופשות שלנו לפי מטבעות:**\n\n`;
                
                Object.keys(currencyBreakdown).forEach(currency => {
                    const data = currencyBreakdown[currency];
                    const minPrice = Math.min(...data.prices);
                    const maxPrice = Math.max(...data.prices);
                    
                    currencyResponse += `${getCurrencySymbol(currency)} **${currency}**: ${data.count} חופשות\n`;
                    currencyResponse += `   טווח מחירים: ${minPrice}-${maxPrice}\n\n`;
                });
                
                currencyResponse += `💡 דוגמאות לחיפוש:\n• "2 דולר"\n• "עד 500 יורו"\n• "100 שקל"`;
                
                return currencyResponse;
                
            default:
                return `❓ פקודה לא מוכרת: ${input}\n\nכתוב /help לרשימת הפקודות הזמינות.`;
        }
    };

    // פונקציות טיפול בשאלות
    const handleDateQuery = (originalInput, input) => {
        // חיפוש תאריכים בטקסט
        const dateMatches = originalInput.match(/\d{1,2}\/\d{1,2}\/?\d{0,4}|\d{4}-\d{2}-\d{2}/g);
        
        if (dateMatches && dateMatches.length >= 1) {
            const searchDate = dateMatches[0];
            const matchingVacations = vacations.filter(vacation => {
                const startDate = new Date(vacation.vacation_start);
                const endDate = new Date(vacation.vacation_ends);
                const queryDate = new Date(searchDate);
                return queryDate >= startDate && queryDate <= endDate;
            });
            
            if (matchingVacations.length > 0) {
                let response = t(
                    `מצאתי ${matchingVacations.length} חופשות שמתאימות לתאריך ${searchDate}:\n\n`,
                    `I found ${matchingVacations.length} vacations that match the date ${searchDate}:\n\n`
                );
                matchingVacations.slice(0, 3).forEach((vacation, index) => {
                    response += `${index + 1}. **${vacation.country_name}**\n`;
                    response += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n`;
                    response += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n`;
                    response += `   📝 ${vacation.vacation_description.substring(0, 100)}...\n\n`;
                });
                
                if (matchingVacations.length > 3) {
                    response += t(
                        `ויש עוד ${matchingVacations.length - 3} חופשות נוספות! אתה יכול לראות את כולן בדף החופשות.`,
                        `And there are ${matchingVacations.length - 3} more vacations! You can see them all on the vacations page.`
                    );
                }
                
                return response;
            } else {
                return t(
                    `לא מצאתי חופשות זמינות בתאריך ${searchDate} 😔\n\nאבל יש לי המלצות אחרות! אתה יכול לבדוק תאריכים אחרים או לראות את כל החופשות הזמינות.`,
                    `I didn't find available vacations on ${searchDate} 😔\n\nBut I have other recommendations! You can check other dates or see all available vacations.`
                );
            }
        }
        
        const availableDates = vacations.map(v => `${v.country_name}: ${v.vacation_start} - ${v.vacation_ends}`).slice(0, 5).join('\n');
        return t(
            `אני יכול לעזור לך למצוא חופשות לפי תאריך! 📅\n\nכמה מהחופשות הזמינות:\n${availableDates}\n\nתוכל לכתוב תאריך ספציפי כמו "15/7/2024" ואני אחפש חופשות שמתאימות.`,
            `I can help you find vacations by date! 📅\n\nSome of the available vacations:\n${availableDates}\n\nYou can write a specific date like "15/7/2024" and I'll search for matching vacations.`
        );
    };

    const handlePriceQuery = (originalInput, input) => {
        // חיפוש מספרים בטקסט למחיר
        const priceMatches = originalInput.match(/\d+/g);
        
        if (priceMatches) {
            const budget = parseInt(priceMatches[0]);
            
            // זיהוי מטבע מהטקסט
            let searchCurrency = 'ILS'; // מטבע ברירת מחדל
            if (input.includes('דולר') || input.includes('dollar') || input.includes('$')) {
                searchCurrency = 'USD';
            } else if (input.includes('יורו') || input.includes('euro') || input.includes('€')) {
                searchCurrency = 'EUR';
            } else if (input.includes('שקל') || input.includes('₪') || input.includes('nis')) {
                searchCurrency = 'ILS';
            } else if (input.includes('פאונד') || input.includes('pound') || input.includes('£')) {
                searchCurrency = 'GBP';
            }
            
            let matchingVacations;
            if (input.includes('עד') || input.includes('מתחת')) {
                matchingVacations = vacations.filter(v => {
                    const vacationCurrency = v.vacation_currency || 'ILS';
                    return vacationCurrency === searchCurrency && v.vacation_price <= budget;
                });
            } else if (input.includes('מעל') || input.includes('יותר')) {
                matchingVacations = vacations.filter(v => {
                    const vacationCurrency = v.vacation_currency || 'ILS';
                    return vacationCurrency === searchCurrency && v.vacation_price >= budget;
                });
            } else {
                // חיפוש בטווח מותאם לפי גודל המחיר
                let tolerance;
                if (budget <= 10) {
                    tolerance = Math.max(budget * 2, 5); // עבור מחירים נמוכים, טווח גדול יותר
                } else if (budget <= 100) {
                    tolerance = budget * 0.8; // 80% עבור מחירים בינוניים
                } else {
                    tolerance = budget * 0.5; // 50% עבור מחירים גבוהים
                }
                
                matchingVacations = vacations.filter(v => {
                    const vacationCurrency = v.vacation_currency || 'ILS';
                    return vacationCurrency === searchCurrency && 
                           Math.abs(v.vacation_price - budget) <= tolerance;
                });
                
                // אם לא נמצאו תוצאות במטבע הספציפי, נחפש בכל המטבעות
                if (matchingVacations.length === 0) {
                    matchingVacations = vacations.filter(v => 
                        Math.abs(v.vacation_price - budget) <= tolerance
                    );
                }
            }
            
            if (matchingVacations.length > 0) {
                let response = t(
                    `מצאתי ${matchingVacations.length} חופשות בטווח המחירים שלך`,
                    `I found ${matchingVacations.length} vacations in your price range`
                );
                if (searchCurrency !== 'ILS') {
                    response += ` (${getCurrencySymbol(searchCurrency)})`;
                }
                response += `:\n\n`;
                
                // מיון לפי מחיר
                matchingVacations.sort((a, b) => a.vacation_price - b.vacation_price);
                
                matchingVacations.slice(0, 3).forEach((vacation, index) => {
                    response += `${index + 1}. **${vacation.country_name}**\n`;
                    response += `   💰 ${vacation.vacation_price} ${getCurrencySymbol(vacation.vacation_currency || 'ILS')}\n`;
                    response += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n`;
                    response += `   📝 ${vacation.vacation_description.substring(0, 80)}...\n\n`;
                });
                
                if (matchingVacations.length > 3) {
                    response += t(
                        `ויש עוד ${matchingVacations.length - 3} חופשות נוספות!`,
                        `And there are ${matchingVacations.length - 3} more vacations!`
                    );
                }
                
                return response;
            } else {
                // חיפוש החופשה הקרובה ביותר במטבע הספציפי
                const sameCurrencyVacations = vacations.filter(v => 
                    (v.vacation_currency || 'ILS') === searchCurrency
                );
                
                if (sameCurrencyVacations.length > 0) {
                    const closestPrice = sameCurrencyVacations.reduce((closest, vacation) => 
                        Math.abs(vacation.vacation_price - budget) < Math.abs(closest.vacation_price - budget) ? vacation : closest
                    );
                    
                    return `לא מצאתי חופשות בדיוק ב-${budget} ${getCurrencySymbol(searchCurrency)} 😔\n\n` +
                           `הכי קרוב זה חופשה ל**${closestPrice.country_name}** ב-${closestPrice.vacation_price} ${getCurrencySymbol(searchCurrency)}\n\n` +
                           `רוצה לראות עוד אפשרויות בטווחי מחירים שונים?`;
                } else {
                    return `לא מצאתי חופשות במטבע ${getCurrencySymbol(searchCurrency)} 😔\n\n` +
                           `אבל יש לנו חופשות נהדרות במטבעות אחרים! תוכל לשאול על מחירים בשקלים או לראות את כל החופשות.`;
                }
            }
        }
        
        // תשובה כללית על מחירים עם פילוח לפי מטבעות
        const currencyBreakdown = {};
        vacations.forEach(v => {
            const currency = v.vacation_currency || 'ILS';
            if (!currencyBreakdown[currency]) {
                currencyBreakdown[currency] = [];
            }
            currencyBreakdown[currency].push(v.vacation_price);
        });
        
        let response = t(
            `הנה פילוח המחירים של החופשות שלנו 💰:\n\n`,
            `Here's the price breakdown of our vacations 💰:\n\n`
        );
        
        Object.keys(currencyBreakdown).forEach(currency => {
            const prices = currencyBreakdown[currency];
            const minPrice = Math.min(...prices);
            const maxPrice = Math.max(...prices);
            const avgPrice = Math.round(prices.reduce((sum, price) => sum + price, 0) / prices.length);
            
            response += `${getCurrencySymbol(currency)} **${currency}**: ${prices.length} ${t('חופשות', 'vacations')}\n`;
            response += `   ${t('טווח', 'Range')}: ${minPrice}-${maxPrice} | ${t('ממוצע', 'Average')}: ${avgPrice}\n\n`;
        });
        
        response += t(
            `💡 תוכל לכתוב:\n• "עד 4000 שקל"\n• "2 דולר"\n• "500 יורו"\n\nואני אמצא לך חופשות מתאימות!`,
            `💡 You can write:\n• "up to 4000 shekels"\n• "2 dollars"\n• "500 euros"\n\nAnd I'll find matching vacations for you!`
        );
        
        return response;
    };

    // פונקציה לקבלת סמל מטבע
    const getCurrencySymbol = (currency) => {
        const symbols = {
            'USD': '$',
            'EUR': '€',
            'ILS': '₪',
            'GBP': '£'
        };
        return symbols[currency] || currency;
    };

    const handleLocationQuery = (originalInput, input) => {
        const countries = [...new Set(vacations.map(v => v.country_name))];
        
        // חיפוש מדינה ספציפית
        const mentionedCountry = countries.find(country => 
            input.includes(country.toLowerCase()) || 
            input.includes(translateCountryName(country).toLowerCase())
        );
        
        if (mentionedCountry) {
            const countryVacations = vacations.filter(v => v.country_name === mentionedCountry);
            let response = `מצאתי ${countryVacations.length} חופשות ל${mentionedCountry}! 🌍\n\n`;
            
            countryVacations.slice(0, 2).forEach((vacation, index) => {
                response += `${index + 1}. **${vacation.vacation_description.substring(0, 50)}...**\n`;
                response += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n`;
                response += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n\n`;
            });
            
            response += `🔗 לצפייה בכל החופשות - [לחץ כאן לדף החופשות](/vacations)\n\n`;
            return response;
        }
        
        // חיפוש אזורי
        if (input.includes('אירופה') || input.includes('europe')) {
            const europeanCountries = ['Italy', 'France', 'Spain', 'Greece', 'Germany', 'Netherlands'];
            const europeanVacations = vacations.filter(v => 
                europeanCountries.some(country => v.country_name.includes(country))
            );
            
            if (europeanVacations.length > 0) {
                let response = `מצאתי ${europeanVacations.length} חופשות באירופה! 🇪🇺\n\n`;
                const topEuropean = europeanVacations.slice(0, 3);
                topEuropean.forEach((vacation, index) => {
                    response += `${index + 1}. **${vacation.country_name}**\n`;
                    response += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n`;
                    response += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n\n`;
                });
                return response;
            }
        }
        
        // רשימת יעדים זמינים
        return t(
            `אני יכול לעזור לך למצוא חופשות לפי יעד! 🗺️\n\nהיעדים הפופולריים שלנו:\n${countries.slice(0, 8).map(c => `• ${c}`).join('\n')}\n\n💡 תוכל גם לשאול על:\n• חופשות באירופה\n• חופשות בים התיכון\n• חופשות אקזוטיות\n\nעל איזה יעד תרצה לשמוע יותר?`,
            `I can help you find vacations by destination! 🗺️\n\nOur popular destinations:\n${countries.slice(0, 8).map(c => `• ${c}`).join('\n')}\n\n💡 You can also ask about:\n• European vacations\n• Mediterranean vacations\n• Exotic vacations\n\nWhich destination would you like to hear more about?`
        );
    };

    // פונקציה לתרגום שמות מדינות
    const translateCountryName = (country) => {
        const translations = {
            'Israel': 'ישראל',
            'Italy': 'איטליה',
            'France': 'צרפת',
            'Spain': 'ספרד',
            'Greece': 'יוון',
            'Turkey': 'טורקיה',
            'Egypt': 'מצרים',
            'Thailand': 'תאילנד',
            'Japan': 'יפן',
            'USA': 'ארהב',
            'Germany': 'גרמניה',
            'Netherlands': 'הולנד'
        };
        return translations[country] || country;
    };

    const handleGeneralVacationQuery = (originalInput, input) => {
        if (input.includes('המלצה') || input.includes('מה תמליץ')) {
            // המלצות מותאמות אישית
            const topVacations = vacations
                .sort((a, b) => new Date(a.vacation_start) - new Date(b.vacation_start))
                .slice(0, 3);
                
            let response = `הנה ההמלצות שלי לחופשות הקרובות! ⭐\n\n`;
            topVacations.forEach((vacation, index) => {
                response += `${index + 1}. **${vacation.country_name}**\n`;
                response += `   📅 ${vacation.vacation_start} - ${vacation.vacation_ends}\n`;
                response += `   💰 ${vacation.vacation_price} ${vacation.vacation_currency || 'ILS'}\n`;
                response += `   ✨ ${vacation.vacation_description.substring(0, 100)}...\n\n`;
            });
            
            return response;
        }
        
        return `יש לנו ${vacations.length} חופשות מדהימות זמינות! 🏖️\n\nאני יכול לעזור לך למצוא בדיוק מה שאתה מחפש:\n• חיפוש לפי תאריכים\n• מיון לפי מחיר\n• המלצות לפי יעדים\n\nמה מעניין אותך הכי הרבה?`;
    };

    const handleGreeting = () => {
        const greetingsHe = [
            "שלום! איך אני יכול לעזור לך למצוא את החופשה המושלמת? 😊",
            "היי! מה שלומך? בואו נמצא לך חופשה מדהימה! 🌟",
            "אהלן! אני כאן כדי לעזור לך לתכנן את החופשה הבאה שלך 🏖️",
        ];
        const greetingsEn = [
            "Hello! How can I help you find the perfect vacation? 😊",
            "Hi! How are you? Let's find you an amazing vacation! 🌟",
            "Hello! I'm here to help you plan your next vacation 🏖️",
        ];
        const greetings = language === 'he' ? greetingsHe : greetingsEn;
        return greetings[Math.floor(Math.random() * greetings.length)];
    };

    const handleGeneralQuery = (input) => {
        const responsesHe = [
            "מעניין! אני מתמחה בעזרה עם חופשות וטיולים. תוכל לשאול אותי על תאריכים, מחירים או יעדים ספציפיים! 🤔",
            "אני לא בטוח שהבנתי בדיוק... אבל אני כאן כדי לעזור לך עם חופשות! על איזה חופשה אתה חולם? 💭",
            "תוכל לנסח את השאלה בצורה קצת אחרת? אני הכי טוב בעזרה עם בחירת חופשות, תאריכים ומחירים! 🎯"
        ];
        const responsesEn = [
            "Interesting! I specialize in helping with vacations and trips. You can ask me about dates, prices, or specific destinations! 🤔",
            "I'm not sure I understood exactly... but I'm here to help you with vacations! What vacation are you dreaming of? 💭",
            "Could you phrase the question a bit differently? I'm best at helping with vacation selection, dates, and prices! 🎯"
        ];
        const responses = language === 'he' ? responsesHe : responsesEn;
        return responses[Math.floor(Math.random() * responses.length)];
    };

    const clearChat = () => {
        // יצירת הודעת ברכה חדשה
        const welcomeMessage = {
            id: Date.now(),
            type: 'bot',
            content: t(
                'שלום! אני כאן כדי לעזור לך למצוא את החופשה המושלמת 🏖️\n\nאני יכול לעזור לך עם:\n• חיפוש חופשות לפי תאריכים\n• מיון לפי טווח מחירים\n• חיפוש לפי יעד או אזור\n• המלצות מותאמות אישית\n\nמה תרצה לדעת?',
                'Hello! I\'m here to help you find the perfect vacation 🏖️\n\nI can help you with:\n• Search vacations by dates\n• Sort by price range\n• Search by destination or area\n• Personalized recommendations\n\nWhat would you like to know?'
            ),
            timestamp: new Date()
        };
        setMessages([welcomeMessage]);
    };

    const toggleChat = () => {
        setIsOpen(!isOpen);
    };

    const value = {
        isOpen,
        setIsOpen,
        messages,
        isTyping,
        vacations,
        addMessage,
        processUserMessage,
        clearChat,
        toggleChat
    };

    return (
        <ChatContext.Provider value={value}>
            {children}
        </ChatContext.Provider>
    );
};
