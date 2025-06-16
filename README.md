# 🏥 MedWise — Medical Supply Management System

A full-stack web application built using Django and PostgreSQL to efficiently manage medical inventory, suppliers, and order processing in hospitals or pharmacies. Designed with a clean HTML/CSS frontend and a robust Django backend, MedWise provides real-time tracking and role-based access control for smooth healthcare logistics.

---

## 🚀 Features

- 📦 **Inventory Management**  
  Track stock levels, add/update/delete medicine records with expiry and price.

- 🧾 **Order Processing**  
  Create and manage purchase orders from suppliers.

- 🧑‍⚕️ **User Authentication**  
  Login system with Admin and Staff roles.

- 🏭 **Supplier Module**  
  Manage supplier details and assign items.

- 📊 **Report Generation**  
  View current stock, expired items, and order history.

---

## 🛠️ Tech Stack

| Component   | Technology       |
|------------|------------------|
| Language    | Python 3.x       |
| Framework   | Django           |
| Database    | PostgreSQL       |
| Frontend    | HTML, CSS        |
| ORM         | Django ORM       |

---

## 🗃️ Database Schema Overview

Some core models:
- `Medicine`: name, quantity, expiry_date, price
- `Supplier`: name, contact info
- `Order`: medicine, supplier, quantity, status
- `User`: username, role (admin/staff)

Django's ORM handles schema migrations and relations.

---

## 🧑‍💻 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/sangeethsgit/MedWise.git
cd MedWise

python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'medwise',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MedWise/
├── medwise/             # Main Django app
├── templates/           # HTML templates
├── static/              # CSS, images
├── db.sqlite3           # (if fallback to SQLite)
├── manage.py
├── requirements.txt
└── README.md
