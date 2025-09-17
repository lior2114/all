# בניית מרובת שלבים
FROM node:20 AS builder

# הגדרת תיקיית עבודה
WORKDIR /app

# העתקת קבצי החבילות
COPY package*.json ./

# התקנת תלויות
RUN npm install 

# העתקת קוד המקור
COPY . ./

# בניית האפליקציה
RUN npm run build

# שלב הפרודקשן עם nginx
FROM nginx:alpine 

# העתקת האפליקציה הבנויה ל-nginx
COPY --from=builder /app/dist /usr/share/nginx/html

# העתקת הגדרות nginx
RUN echo 'server { \
    listen 80; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html index.htm; \
        try_files $uri $uri/ /index.html; \
    } \
}' > /etc/nginx/conf.d/default.conf

# חשיפת פורט
EXPOSE 80

# הפעלת nginx
CMD ["nginx", "-g", "daemon off;"]
