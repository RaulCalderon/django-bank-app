# 🏦 API Bank - Django + PostgreSQL + Docker

This project is an API REST for a basic banking system that allows you to manage clients, accounts and transfers. It is developed with Django and Django REST Framework. It is also containerized with Docker.

---

## ✅ Technologies used in this project:

- Python 3.10+
- Django 5.2.1
- Django REST Framework
- PostgreSQL 14+
- Docker + Docker Compose

---

## 📁 Estructura del proyecto

django-bank-app/
├── bank/ # Main App
│ ├── models.py # Models: Client, Account, Transfers
│ ├── views.py # DRF ViewSets
│ ├── serializers.py # Serializers
│ └── urls.py # API Routes
├── bank_api/ # Django general settings
│ └── settings.py
├── manage.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

## ⚙️ Install and execute locally

1. **Clone repository**
```bash
git clone https://github.com/RaulCalderon/django-bank-app.git
cd bank_api
```

2. **Create virtual enviroment and install dependencies**
```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt
```

3. **Set Database conection (PostgreSQL local)**
Edit `bank_api/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'banco_db',         # Database name
        'USER': 'bank_user',        # Username
        'PASSWORD': 'bank_pass',    # Password
        'HOST': '127.0.0.1',        # Can be localhost too
        'PORT': '5432',
    }
}
```

4. **Migrate and run the server**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

**API URL: http://127.0.0.1:8000/api/**

# At this point you should see the endpoints and be able to add data without problems.

---

## 🐳 Docker

1. **Make sure you have Docker and Docker Compose installed**
2. **Run the containers**
```bash
docker-compose up --build
```

3. **App available in: http://127.0.0.1:8000/api/**
- PostgreSQL: on container `db` (port 5432)

---

## 🔁 Endpoints

| Resource      | Endpoint                    |
|---------------|-----------------------------|
| Clients       | `/api/clients/`             |
| Accounts      | `/api/accounts/`            |
| Transfers     | `/api/transfers/`           |

You can test them with Postman, curl or from the web browser.







