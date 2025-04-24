# Bookstore Management System 📚✏️ 

A Django-based full stack web application that allows users to browse and purchase books. Admins can manage the book inventory via a custom-built admin panel. The project uses Django sessions for cart management, and avoids Django forms and admin.

---

## Tech Stack 🔧

- Backend: Django
- Frontend: HTML, CSS, JavaScript

- DevOps: Docker, Docker Compose, Jenkins 

---

## Features 🌟 

### Authentication 🔒 
- User Registration 
- User Login/Logout

### User Functionality 🛒 
- Browse all available books
- View individual book details
- Add books to cart 

### Admin Panel 🛠️
- Custom admin dashboard
- Add/Edit/Delete books

---

## Docker & Jenkins 🐋 

### Docker
- `Dockerfile` included for app containerization
- `docker-compose.yml` for simplified local setup

### Jenkins
- `Jenkinsfile` included for automated build, test, and deploy pipeline

---

## Setup Instructions 🛠️

```bash
# Clone the repository
git clone https://github.com/Kcode727/Bookstore-crud
cd bookstore

# Run using Docker
docker-compose up --build
open at http://localhost:8000/

## Project Structure
Bookstore-crud/
├── bookstore/                   
│   ├── __init__.py
│   ├── pycache/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│   
├── screenshots/
│   ├── Cart.jpg
│   ├── Home.jpg
│   ├── Login.jpg
│   ├── bookDetail.jpg
│   
├── store/                       
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── templates/                       
│   ├── book_detail.html
│   ├── book_list.html
│   ├── cart.html
│   ├── login.html
│   └── register.html
│   
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
├── manage.py
└── requirements.txt

