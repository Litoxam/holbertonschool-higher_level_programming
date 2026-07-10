# Project Flow

This document provides a complete overview of how the API works, from the moment a client sends a request until the server returns a response.

Understanding this workflow makes it easier to understand how the different parts of the project work together.

---

# Overall Architecture

The API acts as an intermediary between the client and the application's resources.

```text
           HTTP Request
+-----------------------------+
|           Client            |
+-----------------------------+
              │
              ▼
+-----------------------------+
|         Flask API           |
+-----------------------------+
│                             │
│ Authentication              │
│ Authorization               │
│ Business Logic              │
│                             │
+-----------------------------+
              │
              ▼
        HTTP Response
```

---

# Authentication Flow

Every protected request follows the same sequence.

```text
Client

↓

HTTP Request

↓

Protected Route

↓

Authentication

↓

Authentication Successful?

↓

No
│
└────────────► 401 Unauthorized

Yes

↓

Execute Route

↓

HTTP Response
```

---

# Basic Authentication Flow

The `/basic-protected` endpoint uses HTTP Basic Authentication.

```text
Client

↓

GET /basic-protected

↓

Authorization Header

↓

Username
Password

↓

verify_password()

↓

User Exists?

↓

Password Correct?

↓

No
│
└────────────► 401 Unauthorized

Yes

↓

Execute Route

↓

Basic Auth: Access Granted
```

The username and password are verified before the route is executed.

If authentication fails, the route function is never called.

---

# Login Flow

The `/login` endpoint authenticates the user and generates a JWT.

```text
Client

↓

POST /login

↓

JSON Body

↓

request.get_json()

↓

Extract Username

Extract Password

↓

Search User

↓

Verify Password

↓

Credentials Valid?

↓

No
│
└────────────► 401 Unauthorized

Yes

↓

create_access_token()

↓

JWT Generated

↓

Return JWT
```

The generated JWT becomes the client's proof of identity.

---

# JWT Authentication Flow

Every JWT-protected route follows this process.

```text
Client

↓

GET /jwt-protected

↓

Authorization Header

↓

Bearer TOKEN

↓

@jwt_required()

↓

Token Validation

↓

Valid?

↓

No
│
└────────────► JWT Error Handler

↓

401 Unauthorized

──────────────

Yes

↓

Execute Route

↓

JWT Auth: Access Granted
```

The token is validated before the route executes.

---

# JWT Validation Process

Flask-JWT-Extended performs several checks automatically.

```text
JWT Received

↓

Signature Valid?

↓

Expired?

↓

Revoked?

↓

Fresh Token Required?

↓

All Checks Passed?

↓

Yes

↓

Route Execution

──────────────

No

↓

JWT Error Handler

↓

401 Unauthorized
```

This entire validation process happens automatically thanks to `@jwt_required()`.

---

# Administrator Flow

The `/admin-only` endpoint introduces authorization.

Authentication alone is no longer sufficient.

```text
Client

↓

JWT Token

↓

@jwt_required()

↓

Token Valid?

↓

No

↓

401 Unauthorized

──────────────

Yes

↓

get_jwt_identity()

↓

Retrieve User

↓

Role == admin ?

↓

No

↓

403 Forbidden

──────────────

Yes

↓

Admin Access: Granted
```

This demonstrates the difference between **authentication** and **authorization**.

---

# Complete Request Lifecycle

The following diagram summarizes the entire project.

```text
Client

↓

Request

↓

Flask Route

↓

Authentication

↓

Authentication Successful?

↓

No

↓

401 Unauthorized

──────────────

Yes

↓

Authorization Needed?

↓

No

↓

Execute Route

↓

200 OK

──────────────

Yes

↓

Role Verification

↓

Role Allowed?

↓

No

↓

403 Forbidden

──────────────

Yes

↓

Execute Route

↓

200 OK
```

---

# How the Components Work Together

The project is composed of several independent components.

Each one has a specific responsibility.

```text
Flask
│
├── Creates the application
├── Defines routes
└── Handles requests

HTTPBasicAuth
│
├── Reads credentials
├── Calls verify_password()
└── Grants or denies access

JWTManager
│
├── Generates JWTs
├── Validates JWTs
└── Calls JWT error handlers

Users Dictionary
│
├── Stores usernames
├── Stores hashed passwords
└── Stores user roles

Routes
│
├── /basic-protected
├── /login
├── /jwt-protected
└── /admin-only
```

Each component focuses on a single responsibility, making the application easier to understand and maintain.

---

# End-to-End Example

A complete interaction with the API looks like this.

```text
1. Client logs in

↓

POST /login

↓

JWT Returned

↓

2. Client stores JWT

↓

3. Client accesses protected route

↓

GET /jwt-protected

↓

Bearer TOKEN

↓

200 OK

↓

4. Client accesses admin route

↓

GET /admin-only

↓

Role Verified

↓

200 OK or 403 Forbidden
```

---

# Summary

The project demonstrates the complete lifecycle of a secure REST API.

Starting from a simple HTTP request, the application:

* authenticates the client;
* validates credentials or tokens;
* authorizes access when required;
* executes the requested route;
* returns the appropriate HTTP response.

By combining Flask, Basic Authentication, JWT authentication, and Role-Based Access Control, the application illustrates the core principles used in modern API security.
