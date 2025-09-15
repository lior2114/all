# Project Structure Rules Prompt (with Component Folders and Progress Tracking)

You are an AI assistant responsible for generating and organizing project structures for **React (frontend)** and **Flask with SQL (backend)**.  
Follow these rules strictly when creating or modifying project files.  

---

## FRONTEND (React)

### 1. Folder Structure
- Ensure the following folders exist (create if missing):  
  ```
  api/
  Contexts/
  Components/
  Pages/
  ```

- The folder hierarchy must follow this order:  
  ```
  api → Contexts → Components → Pages
  ```

### 2. CSS Rules
- For any file requiring CSS, use only the naming convention:  
  ```
  styles.<eventName>
  ```
- For every `.jsx` (or similar) file created:  
  - Also create a corresponding CSS module file named:  
    ```
    <filename>.css.module
    ```
  - Both the `.jsx` file and its `.module.css` file must be placed in a **dedicated folder** named after the component/file.  

### Example Skeleton
```
frontend/
│
├── api/
│   └── api.js
│
├── Contexts/
│   └── AppContext/
│       ├── AppContext.jsx
│       └── AppContext.module.css
│
├── Components/
│   └── Navbar/
│       ├── Navbar.jsx
│       └── Navbar.module.css
│
├── Pages/
│   └── Home/
│       ├── Home.jsx
│       └── Home.module.css
│
└── index.js
```

---

## BACKEND (Flask + SQL)

### 1. Folder Structure
- Create the following folders and files:  
  ```
  backend/
  ├── modules/
  │   └── users_module.py
  │
  ├── controller/
  │   └── users_controller.py
  │
  ├── routes/
  │   └── users_routes.py
  │
  └── app.py
  ```

### 2. Folder Responsibilities
- **modules/**  
  - Contains only **table definitions and SQL operations** (insert, update, delete).  
- **controller/**  
  - Contains all **business logic and error handling**.  
  - Must:  
    - Use `request.get_json()` for data extraction.  
    - Implement error handling (`if not ...: raise error`).  
    - Handle `hashpassword` and `token` where required.  
- **routes/**  
  - Contains only **Flask Blueprints**.  
  - Must import functions from `controller`.  
  - Define endpoints with proper headers.  
- **app.py**  
  - Contains only:  
    - Imports of `modules` and `routes`  
    - Initialization of all database tables  

---

### Example Skeleton

**modules/users_module.py**
```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

def add_user(username, password_hash):
    new_user = User(username=username, password=password_hash)
    db.session.add(new_user)
    db.session.commit()
    return new_user
```

**controller/users_controller.py**
```python
from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from modules.users_module import add_user, User, db

def create_user():
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Invalid request"}), 400
    
    password_hash = generate_password_hash(data["password"])
    user = add_user(data["username"], password_hash)
    return jsonify({"message": "User created", "id": user.id}), 201
```

**routes/users_routes.py**
```python
from flask import Blueprint
import controller.users_controller as C

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["POST"])
def create_user_route():
    return C.create_user()
```

**app.py**
```python
from flask import Flask
from modules.users_module import db
from routes.users_routes import users_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True)
```

---

## PROGRESS TRACKING

1. Create a folder named:  
   ```
   progress/
   ```

2. Inside this folder, create a file named:  
   ```
   progress.md
   ```

3. Every time the project changes, append a new entry to `progress.md` describing the latest progress.  
   - This file acts as a **log history** of the project.  
   - The AI must always **read from this file before executing any new command**, so it remembers previous actions.  

### Example Skeleton
```
progress/
   progress.md
```

**progress/progress.md**
```markdown
# Project Progress Log

## [2025-09-13]
- Created initial project structure for frontend and backend
- Added Navbar component and Home page with their CSS modules
- Set up basic Flask app with users module, controller, and routes
```
