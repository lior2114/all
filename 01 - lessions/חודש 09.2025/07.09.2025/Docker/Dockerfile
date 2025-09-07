#install the linux alpine 3.19
#FROM alpine:3.19

#install the python3 and alpine
FROM python:alpine3.19

# 📂 הגדרת תיקיית עבודה (Working Directory) בתוך הקונטיינר
# כל הפקודות הבאות (COPY, RUN, CMD וכו') ירוצו מתוך /app
# זה עוזר לנו לסדר את הקבצים במקום קבוע בתוך הקונטיינר.
WORKDIR /app

# 📥 מעתיקים את כל הקבצים מהמחשב המקומי (התיקייה הנוכחית עם Dockerfile)
# אל תוך התיקייה /app בתוך הקונטיינר.
# לדוגמה: אם יש לנו app.py במחשב, הוא יעבור ל־/app/app.py בקונטיינר.
COPY . /app

# 🚀 מגדירים את פקודת ההרצה (ENTRYPOINT) ברגע שהקונטיינר עולה.
# כאן אנחנו מריצים python3 עם הקובץ app.py
# כך שכל פעם שהקונטיינר יופעל → התוכנית הראשית שלנו תתחיל לרוץ.
ENTRYPOINT ["python", "app.py"]

