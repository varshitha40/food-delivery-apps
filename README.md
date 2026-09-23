# 🍔 Food Delivery App

A simple and user-friendly Food Delivery Web Application developed using Python and Flask. The application allows users to browse food items, add items to a cart, and place food orders through an easy-to-use interface.

## 📌 Project Overview

The Food Delivery App is designed to provide a basic online food ordering experience. Users can browse the available food items, manage their cart, and proceed to checkout.

This project was developed as part of my internship/project work to gain practical experience in web application development, database management, and user authentication.

## ✨ Features

- 👤 User Registration
- 🔐 User Login and Logout
- 🍽️ Browse Food Items
- 🏪 View Restaurants
- 🛒 Add Food Items to Cart
- ➕ Manage Cart Items
- 💳 Checkout Page
- 📦 Place Food Orders
- ✅ Order Success Page
- 🗄️ Database Integration
- 🎨 Simple and User-Friendly Interface

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-Login**
- **HTML**
- **CSS**
- **SQLite**
- **Jinja2**

## 📂 Project Structure

```text
food_delivery_app/
│
├── app/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── menu.html
│   │   ├── restaurants.html
│   │   ├── cart.html
│   │   ├── checkout.html
│   │   └── order_success.html
│   │
│   ├── static/
│   │   └── style.css
│   │
│   ├── models.py
│   ├── routes.py
│   └── __init__.py
│
├── database.db
├── requirements.txt
├── run.py
└── seed.py
