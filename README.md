# 🔐 Mini Authentication System

A terminal-based authentication system built in Python that demonstrates how real authentication systems work internally before introducing web frameworks like Flask or FastAPI.

This project is part of the **CyberSpec Roadmap**, focusing on secure authentication design, password hashing, validation, storage abstraction, and automated testing.

---

## Features

- User Registration
- User Login
- Secure Password Hashing (bcrypt)
- Password Verification
- Username Validation
- Password Validation
- Duplicate Username Detection
- User Storage using JSON
- Last Login Tracking
- Automated Unit Tests (pytest)
- Modular Architecture

---

## Project Structure

```text
Mini-Authentication-System/
│
├── auth/
│   ├── __init__.py
│   ├── register.py
│   ├── login.py
│   └── validator.py
│
├── database/
│   ├── __init__.py
│   ├── storage.py
│   └── users.json
│
├── models/
│   ├── __init__.py
│   └── user.py
│
├── security/
│   ├── __init__.py
│   └── password_hasher.py
│
├── tests/
│   ├── __init__.py
│   └── test_auth.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Authentication Flow

```
User
 │
 ▼
Enter Username & Password
 │
 ▼
Validate Input
 │
 ▼
Check Duplicate User
 │
 ▼
Hash Password (bcrypt)
 │
 ▼
Store User
```

### Login Flow

```
User
 │
 ▼
Enter Username & Password
 │
 ▼
Find User
 │
 ▼
Verify Password
 │
 ▼
Update Last Login
 │
 ▼
Authentication Successful
```

---

# Security Features

## Password Hashing

Passwords are never stored in plaintext.

The project uses **bcrypt** to securely hash passwords before storing them.

Example:

```
Password123!

↓

$2b$12$...
```

---

## Password Verification

Authentication uses bcrypt's verification function instead of hashing passwords manually.

```
Entered Password

↓

bcrypt.checkpw()

↓

True / False
```

---

## Username Validation

- Minimum 3 characters
- Maximum 20 characters
- Letters
- Numbers
- Underscores only

---

## Password Validation

Current project policy:

- Minimum length requirement
- Additional complexity rules can be configured by modifying `validator.py`

---

## Storage Layer

The application separates storage from authentication logic.

Authentication modules never access `users.json` directly.

```
Register/Login
      │
      ▼
Storage Layer
      │
      ▼
users.json
```

This abstraction allows replacing JSON with SQLite or PostgreSQL in the future without changing authentication logic.

---

## Project Architecture

```
                   CLI
                    │
                    ▼
      ┌────────────────────────┐
      │ Authentication Engine  │
      └────────────────────────┘
         │        │         │
         ▼        ▼         ▼
 Validation   Password   Storage
              Hasher      Layer
         │                 │
         └────────┬────────┘
                  ▼
              users.json
```

---

# Running the Project

## Clone

```bash
git clone <repository-url>
cd Mini-Authentication-System
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python main.py
```

---

## Run Tests

```bash
pytest
```

Expected output:

```
7 passed
```

---

# Concepts Learned

- Authentication vs Authorization
- Password Hashing
- bcrypt
- Password Verification
- Storage Abstraction
- Separation of Concerns
- Secure Registration Flow
- Secure Login Flow
- User Validation
- Threat Modeling
- Modular Software Design
- Dataclasses
- JSON Storage
- Automated Testing
- Fail Fast Principle
- Security-focused API Design

---

# Future Improvements

- SQLite / PostgreSQL Backend
- Password Reset
- Multi-Factor Authentication (MFA)
- JWT Authentication
- Session Management
- Account Lockout
- Rate Limiting
- Password Strength Analyzer Integration
- Logging & Audit Trails
- Email Verification
- Role-Based Access Control (RBAC)

---

# Technologies Used

- Python 3.12
- bcrypt
- pytest

---

# Learning Outcomes

By completing this project, I learned how professional authentication systems are designed before introducing web frameworks.

The project demonstrates:

- Secure password storage
- Authentication workflows
- Password verification
- Modular software architecture
- Defensive programming
- Security-first design
- Automated testing

This project serves as a foundation for future authentication systems built with FastAPI, Flask, Django, or other backend frameworks.

---

## License

This project is built for educational purposes as part of the CyberSpec cybersecurity roadmap.