# 🛡️ Flask User Management API

A lightweight and powerful **Flask REST API** for managing users, workspaces, and super admins — perfect for SaaS platforms, internal tools, or hobby projects!

---

## 📋 Features

- 🔐 **Authentication** — Secure user login and signup (JWT-based authentication).
- 🏢 **Workspace Creation** — Users can create and manage their own workspaces.
- 👤 **User Profile Management** — Update profiles, change passwords, manage settings.
- 🛠️ **Super Admin Panel** — Full control over users and workspaces.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the project root and add:
```
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
JWT_SECRET_KEY=your_jwt_secret
```

### 4. Run the Application
```bash
flask run
```

> The API will be available at `http://localhost:5000/`

---

## 📚 API Endpoints Overview

| Method | Endpoint | Description |
|:------:|:---------|:------------|
| POST   | `/auth/signup`   | Register a new user |
| POST   | `/auth/login`    | Authenticate user and get token |
| POST   | `/workspace/create` | Create a new workspace |
| GET    | `/profile`       | Get user profile |
| PUT    | `/profile/update`| Update user profile |
| GET    | `/admin/users`   | (Super Admin) List all users |

> (More detailed API documentation coming soon!)

---

## 🛠️ Technologies Used

- **Flask** — Web framework
- **Flask-JWT-Extended** — Authentication
- **Flask-SQLAlchemy** — ORM for database models
- **PostgreSQL** (or your choice) — Database
- **python-dotenv** — Environment variable management

---

## 📦 Project Structure

```
/app
    /auth
    /workspace
    /profile
    /admin
    models.py
    utils.py
    __init__.py
config.py
run.py
requirements.txt
README.md
```

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to change.

If you like this project, ⭐️ star it — it helps a lot!

---

## 📬 Contact

For any feedback, ideas, or collaborations:

- GitHub: [your-username](https://github.com/your-username)
- Email: your.email@example.com

---

> Built with ❤️ using Flask ✨
