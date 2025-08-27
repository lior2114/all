# Vacation App - Python Full Stack Project

This is a vacation management system built with Python and Flask as part of a full stack development course (John Bryce, 2025).

It allows users to register, log in, view available vacations, and like or unlike them. Admin users (manually inserted) can manage all vacation entries and users.

---

## Roles

- **Admin**: Can create, update, and delete vacations and users (Admins must be seeded manually).
- **User**: Can register, log in, view vacations, and like/unlike them.

---

## Technologies Used

- Python 3
- Flask
- SQLite
- Postman (for API testing)

---

## Project Structure

```
vacation_app/
├── app.py                   # Main file to start the server
├── my_db.db                 # SQLite database
├── requirements.txt         # Python dependencies
├── models/                  # Data access layer
├── controllers/             # Business logic and validation
├── routes/                  # API endpoints using Flask blueprints
├── seed_data.py             # Script to populate roles, countries, admin, and demo vacations
└── venv/                    # Virtual environment (not included)
```

---

## Setup Instructions

1. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server to create the database and tables:

```bash
python app.py
```

4. (Optional) Populate roles, countries, admin user, and demo vacations:

```bash
python vacation_app/seed_data.py
```

> Make sure `app.py` has been run once to create all tables before using `seed_data.py`.

---

## Postman API Endpoints

### Authentication

- `POST /register` – Register a new user (always created with role "User")
- `POST /login` – Log in with email and password

### Vacations

- `GET /vacations` – List all vacations (sorted by start date, including past ones)
- `GET /vacations/<id>` – Get vacation by ID
- `POST /vacations` – Create a vacation (admin only)
- `PUT /vacations/<id>` – Update a vacation (admin only)
- `DELETE /vacations/<id>` – Delete a vacation (admin only)

### Likes

- `POST /likes` – Like a vacation
- `DELETE /likes` – Unlike a vacation
- `GET /likes/<user_id>` – List all vacations liked by a user

### Countries

- `GET /countries` – Get all available countries

### Users

- `GET /users` – List all users
- `GET /users/<id>` – Get a user by ID
- `PUT /users/<id>` – Update user information
- `DELETE /users/<id>` – Delete a user

---

## Notes

- The database includes:
  - Two roles: Admin and User
  - An admin user (inserted via seed script)
  - A predefined list of 10 countries
  - At least 12 demo vacations (via seed script)
  - An empty likes table on initial setup
- Admins cannot be registered via API – they must be manually inserted (via seed or SQL)
- `start_date` must be today or later for new vacations
- `end_date` must be after `start_date`
- Price must be a number between 0 and 10,000
- Email validation and uniqueness is enforced
