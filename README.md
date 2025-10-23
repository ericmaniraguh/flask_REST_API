
---

# 🧩 Flask RESTful API Application

This project is a simple **Flask-based RESTful API** designed for learning and experimentation with Flask, Flask-RESTful, and Flask-SQLAlchemy. The goal is to build a clean, modular API that can later be extended with more endpoints, database models, and integrations.

---

## 🚀 Getting Started

### 1️⃣ Create and Activate a Virtual Environment

```bash
# Create virtual environment
py -m venv .venv

# Activate it
source .venv/Scripts/activate
```

> 💡 On Windows PowerShell, use:
>
> ```bash
> .venv\Scripts\Activate.ps1
> ```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install them:

```bash
pip install Flask Flask-RESTful Flask-SQLAlchemy
```

---

## 📦 Project Dependencies

Below are the current dependencies used in this project:

```
aniso8601==9.0.1
blinker==1.8.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
Flask-RESTful==0.3.10
Flask-SQLAlchemy==3.1.1
greenlet==3.0.3
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==2.1.5
pytz==2024.1
six==1.16.0
SQLAlchemy==2.0.30
typing_extensions==4.12.2
Werkzeug==3.0.3
```

---

## 🧠 Project Overview

The project demonstrates how to:

* Set up a **Flask RESTful API** using `Flask-RESTful`
* Integrate a **SQLAlchemy ORM** for database management
* Structure Flask projects for scalability
* Handle **CRUD (Create, Read, Update, Delete)** operations

---

## 🧪 Running the Application

After activating the virtual environment and installing dependencies:

```bash
python app.py
```

Visit the API in your browser or API client (like Postman):

```
http://127.0.0.1:5000/
```

---

## 🧰 Folder Structure (Suggested)

```
flask-API/
│
├── app.py
├── models/
│   └── __init__.py
├── resources/
│   └── __init__.py
├── .venv/
├── requirements.txt
└── README.md
```

---

## 🧩 Next Steps

* [ ] Add sample routes/endpoints
* [ ] Connect to a database
* [ ] Implement CRUD functionality
* [ ] Add error handling and validation
* [ ] Write tests and documentation

---

## 👨‍💻 Author

**Eric Maniraguha**


---
