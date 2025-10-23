

---

# Flask RESTful API Application

This project is a simple **Flask-based RESTful API** designed for learning and experimentation with Flask, Flask-RESTful, and Flask-SQLAlchemy. The goal is to build a clean, modular API that supports **CRUD operations**, including full and partial updates.

---

## Getting Started

### 1. Create and Activate a Virtual Environment

```bash
# Create virtual environment
py -m venv .venv

# Activate it
source .venv/Scripts/activate
```

> On Windows PowerShell:
>
> ```bash
> .venv\Scripts\Activate.ps1
> ```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install Flask Flask-RESTful Flask-SQLAlchemy
```

---

## Project Dependencies

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

## Project Overview

This API demonstrates how to:

* Set up a **Flask RESTful API** using `Flask-RESTful`
* Integrate **SQLAlchemy ORM** for database management
* Handle **CRUD (Create, Read, Update, Delete)** operations:

  * **GET /api/users/** → Get all users
  * **POST /api/users/** → Create single or multiple users
  * **GET /api/users/<id>** → Get a user by ID
  * **PUT /api/users/<id>** → Full update of a user
  * **PATCH /api/users/<id>** → Partial update of a user
  * **DELETE /api/users/<id>** → Delete a user

---

## Example Requests

### GET all users

```
GET http://127.0.0.1:5000/api/users/
```

### POST single user

```json
{
  "username": "ericmaniraguha",
  "email": "eric.maniraguha@example.com"
}
```

### POST multiple users

```json
[
  { "username": "johndoe", "email": "johndoe@example.com" },
  { "username": "janedoe", "email": "janedoe@example.com" }
]
```

### PUT user (full update)

```json
{
  "username": "newusername",
  "email": "newemail@example.com"
}
```

### PATCH user (partial update)

```json
{
  "email": "partialupdate@example.com"
}
```

### DELETE user

```
DELETE http://127.0.0.1:5000/api/users/2
```

---

## Folder Structure (Suggested)

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

## Running the Application

After activating the virtual environment and installing dependencies:

```bash
python app.py
```

Access in browser or Postman:

```
http://127.0.0.1:5000/
```

---

## Author

**Eric Maniraguha**

---

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

```
MIT License

Copyright (c) 2025 Eric Maniraguha

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

