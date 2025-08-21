# ERP Backend (Django + PostgreSQL)

This repository contains the backend for the ERP system built with **Django**, **Django REST Framework**, and **PostgreSQL**.  
Authentication is handled using **JWT** via `djangorestframework-simplejwt`.  

---

## 🚀 Features
- Django 5 + Django REST Framework
- Custom `User` model (`accounts.User`)
- JWT Authentication (login, refresh, blacklist)
- PostgreSQL database
- CORS support for frontend
- Auto superuser creation (Render deployment ready)

---

## 📦 Installation (Local Development)

### 1. Clone the repository
```bash
git clone https://github.com/your-username/erp-backend.git
cd erp-backend
````

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=*

# Database
POSTGRES_DB=erp
POSTGRES_USER=erpuser
POSTGRES_PASSWORD=erppass
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# CORS (Frontend URL)
CORS_ALLOWED_ORIGINS=http://localhost:5173
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (local only)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

---

## 📂 Project Structure

```
core/                # Django project config
  ├── settings.py
  ├── urls.py
  ├── wsgi.py
  └── asgi.py
accounts/            # Custom User model + auth APIs
requirements.txt     # Python dependencies
manage.py            # Django management CLI
```

---

## 🔑 API Authentication

* All APIs are protected by **JWT Authentication**.
* Obtain tokens via login endpoint, then include:

  ```
  Authorization: Bearer <your_token>
  ```

---

## ✅ Requirements

* Python 3.10+
* PostgreSQL 13+
* pip

---

Deployed Url : https://erp-rbac-backend.onrender.com