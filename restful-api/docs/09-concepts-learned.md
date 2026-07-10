# Concepts Learned

This document summarizes the main concepts introduced throughout this project.

Understanding these concepts is essential for building secure REST APIs.

---

# REST API

A REST API (Representational State Transfer) is a web service that allows different applications to communicate through HTTP requests.

Clients send requests.

Servers process those requests and return responses.

Example:

```text
Client

↓

GET /jwt-protected

↓

Server

↓

Response
```

REST APIs are widely used because they are simple, scalable, and language-independent.

---

# Flask

Flask is a lightweight Python web framework.

It provides everything needed to create web applications and REST APIs.

In this project, Flask is responsible for:

* creating the application;
* defining routes;
* receiving HTTP requests;
* returning HTTP responses.

---

# Routing

A route maps a URL to a Python function.

Example:

```python
@app.route("/login", methods=["POST"])
def post_login():
```

Whenever a client sends a `POST` request to `/login`, Flask automatically executes `post_login()`.

---

# HTTP Methods

This project uses two HTTP methods.

## GET

Retrieves data from the server.

Examples:

* `/basic-protected`
* `/jwt-protected`
* `/admin-only`

---

## POST

Sends data to the server.

Example:

* `/login`

---

# JSON

JSON (JavaScript Object Notation) is the standard format used to exchange information between clients and servers.

Example:

```json
{
    "username": "user1",
    "password": "password"
}
```

Flask converts incoming JSON into Python dictionaries with:

```python
request.get_json()
```

---

# jsonify()

`jsonify()` converts Python dictionaries into JSON responses.

Example:

```python
return jsonify({
    "access_token": token
})
```

This automatically creates a valid JSON response and sets the correct HTTP headers.

---

# Basic Authentication

Basic Authentication requires the client to send:

* username
* password

with every request.

The credentials are transmitted inside the `Authorization` header.

Example:

```text
Authorization: Basic dXNlcjE6cGFzc3dvcmQ=
```

Flask-HTTPAuth automatically verifies these credentials before granting access.

---

# Password Hashing

Passwords should never be stored in plain text.

Instead, they are transformed into hashes.

Example:

```python
generate_password_hash(password)
```

This produces a secure string that cannot easily be converted back into the original password.

---

# Password Verification

When a user logs in, the entered password must be compared with the stored hash.

Example:

```python
check_password_hash(user["password"], password)
```

This verifies the password without exposing the original value.

---

# JWT Authentication

JWT (JSON Web Token) allows users to authenticate once and receive a secure token.

Instead of sending their username and password with every request, clients send:

```text
Authorization: Bearer TOKEN
```

The server validates this token before executing protected routes.

---

# JWT Secret Key

Every JWT is digitally signed.

The secret key is responsible for generating and verifying that signature.

Example:

```python
app.config["JWT_SECRET_KEY"] = "your_secret_key"
```

If the token is modified, its signature becomes invalid and authentication fails.

---

# JWT Identity

When creating a token:

```python
create_access_token(identity=username)
```

the username is stored inside the JWT.

Later:

```python
get_jwt_identity()
```

retrieves that username.

This allows the application to identify the authenticated user.

---

# Decorators

Decorators execute code before a function.

This project uses two authentication decorators.

Basic Authentication:

```python
@auth.login_required
```

JWT Authentication:

```python
@jwt_required()
```

Decorators simplify route protection by handling authentication automatically.

---

# Authentication

Authentication answers one question:

> **Who are you?**

Examples:

* username/password;
* JWT token.

If authentication succeeds, the request continues.

Otherwise:

```text
401 Unauthorized
```

is returned.

---

# Authorization

Authorization answers another question:

> **What are you allowed to do?**

Even after a user has been authenticated, access may still be denied if the required permissions are missing.

Example:

```text
Role = user

↓

GET /admin-only

↓

403 Forbidden
```

---

# Role-Based Access Control (RBAC)

RBAC restricts access according to a user's role.

In this project:

| Role  | Permissions                                                     |
| ----- | --------------------------------------------------------------- |
| user  | Access authenticated endpoints                                  |
| admin | Access authenticated endpoints and administrator-only endpoints |

This approach makes applications more secure and easier to maintain.

---

# HTTP Headers

HTTP headers provide additional information about requests and responses.

Examples used in this project:

Basic Authentication:

```text
Authorization: Basic BASE64_CREDENTIALS
```

JWT Authentication:

```text
Authorization: Bearer JWT_TOKEN
```

Headers allow authentication data to be transmitted without placing it inside the request body.

---

# HTTP Status Codes

Three status codes are used throughout the project.

| Code                 | Meaning                                             |
| -------------------- | --------------------------------------------------- |
| **200 OK**           | Request completed successfully.                     |
| **401 Unauthorized** | Authentication failed.                              |
| **403 Forbidden**    | Authentication succeeded, but authorization failed. |

Using the correct status codes makes an API easier to understand and debug.

---

# Authentication Workflow

The complete authentication process follows these steps:

```text
Client

↓

Login

↓

Verify Credentials

↓

Generate JWT

↓

Client Stores Token

↓

Protected Request

↓

Validate JWT

↓

Retrieve User

↓

Check Role

↓

Grant or Deny Access
```

---

# Key Takeaways

By completing this project, you learned how to:

* build REST APIs using Flask;
* create and protect API endpoints;
* hash and verify passwords securely;
* implement Basic Authentication;
* generate and validate JWT tokens;
* authenticate users with Bearer tokens;
* retrieve information stored inside JWTs;
* implement Role-Based Access Control (RBAC);
* distinguish Authentication from Authorization;
* return appropriate HTTP status codes;
* handle JWT authentication errors consistently.

These concepts form the foundation of secure REST API development and are widely used in modern web applications.

---

# Conclusion

This project demonstrates the complete authentication lifecycle of a REST API.

Starting with Basic Authentication, it progresses toward JWT-based authentication and finally introduces authorization through user roles.

Although simplified by using an in-memory user database, the architecture closely reflects how authentication and authorization are implemented in real-world applications.

The techniques learned here can easily be extended to production environments using databases, stronger secret management, HTTPS, refresh tokens, and more advanced authorization strategies.
