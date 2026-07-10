# Project Overview

## Introduction

This project demonstrates how to secure a REST API using Flask.

The application implements two common authentication mechanisms:

- **Basic HTTP Authentication**
- **JSON Web Token (JWT) Authentication**

It also introduces **Role-Based Access Control (RBAC)** to restrict access to specific resources depending on a user's role.

Instead of using a database, users are stored in memory inside a Python dictionary. This keeps the project simple while focusing on API security concepts.

---

# Project Objectives

The main objectives of this project are to:

- Build a REST API using Flask.
- Understand how authentication works.
- Protect endpoints from unauthorized access.
- Generate and validate JWT tokens.
- Restrict access based on user roles.
- Return appropriate HTTP status codes.
- Handle authentication errors properly.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Programming language |
| Flask | Web framework |
| Flask-HTTPAuth | Basic Authentication |
| Flask-JWT-Extended | JWT Authentication |
| Werkzeug | Password hashing and verification |

---

# Project Structure

```text
.
├── docs/
│   ├── 01-project-overview.md
│   ├── 02-flask-basics.md
│   ├── 03-basic-authentication.md
│   ├── 04-jwt-authentication.md
│   ├── ...
│
├── task_05_basic_security.py
└── README.md
```

---

# API Endpoints

The application exposes four endpoints.

| Method | Endpoint | Authentication | Description |
|---------|----------|----------------|-------------|
| GET | `/basic-protected` | Basic Authentication | Protected route using HTTP Basic Authentication |
| POST | `/login` | None | Authenticates a user and returns a JWT token |
| GET | `/jwt-protected` | JWT | Protected route requiring a valid JWT |
| GET | `/admin-only` | JWT + Admin Role | Protected route accessible only to administrators |

---

# Authentication Methods

This project uses two different authentication methods.

## Basic Authentication

Basic Authentication requires the client to send a username and password with every request.

Example:

```text
Authorization: Basic dXNlcjE6cGFzc3dvcmQ=
```

Flask-HTTPAuth automatically verifies these credentials before allowing access to protected resources.

---

## JWT Authentication

JWT (JSON Web Token) allows users to authenticate only once.

After a successful login:

1. The server generates a JWT.
2. The client stores this token.
3. Every future request sends the token inside the `Authorization` header.

Example:

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

The server verifies the token before executing protected routes.

---

# Project Workflow

The API follows the authentication workflow below.

```text
Client

│

├── GET /basic-protected
│       │
│       └── Basic Authentication
│
├── POST /login
│       │
│       └── Receive JWT Token
│
├── GET /jwt-protected
│       │
│       └── JWT Authentication
│
└── GET /admin-only
        │
        ├── JWT Authentication
        └── Role Verification
```

---

# Expected Responses

The API returns different HTTP status codes depending on the authentication result.

| Status Code | Meaning |
|--------------|---------|
| **200 OK** | The request was successful. |
| **401 Unauthorized** | Authentication failed or credentials are missing. |
| **403 Forbidden** | Authentication succeeded, but the user does not have permission to access the resource. |

---

# What You Will Learn

Throughout this project, you will learn how to:

- Build REST APIs with Flask.
- Protect routes using Basic Authentication.
- Authenticate users with JWT.
- Generate secure access tokens.
- Verify hashed passwords.
- Handle JWT errors.
- Restrict access according to user roles.
- Return appropriate HTTP responses.
- Understand the difference between Authentication and Authorization.

---

# Next Step

The next document explains the basics of Flask and the initialization of the application.

📄 **Next file:** `02-flask-basics.md`