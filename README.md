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
