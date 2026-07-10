# JWT Error Handlers

This document explains how JWT authentication errors are handled in the application.

By default, Flask-JWT-Extended already detects invalid or missing tokens.

However, the default error messages do not always match the requirements of this project.

To ensure consistent behavior, custom JWT error handlers are implemented.

---

# Why Use Error Handlers?

Whenever a client accesses a protected route, Flask first validates the JWT.

Several errors may occur:

* No token was provided.
* The token is invalid.
* The token has expired.
* The token has been revoked.
* The route requires a fresh token.

Instead of allowing Flask to return its default responses, the application provides custom responses.

This ensures that every authentication error returns:

```text
401 Unauthorized
```

as required by the project specifications.

---

# How JWT Error Handlers Work

When a protected endpoint is accessed:

```text
Client

↓

GET /jwt-protected

↓

@jwt_required()

↓

Token Validation

↓

Error?

↓

Yes

↓

Corresponding Error Handler

↓

401 Unauthorized
```

The protected route is **never executed** if authentication fails.

---

# Missing Token

```python
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401
```

## Purpose

This handler is called when no JWT is provided in the request.

For example:

```bash
curl http://127.0.0.1:5000/jwt-protected
```

Since no `Authorization` header is present, Flask immediately calls:

```python
handle_unauthorized_error()
```

Response:

```json
{
    "error": "Missing or invalid token"
}
```

Status:

```text
401 Unauthorized
```

---

# Invalid Token

```python
@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401
```

## Purpose

This handler is called when the client sends a malformed or invalid JWT.

Example:

```bash
curl http://127.0.0.1:5000/jwt-protected \
-H "Authorization: Bearer invalid_token"
```

Since the token cannot be verified, Flask executes:

```python
handle_invalid_token_error()
```

Response:

```json
{
    "error": "Invalid token"
}
```

Status:

```text
401 Unauthorized
```

---

# Expired Token

```python
@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401
```

## Purpose

JWTs can have an expiration date.

If a client attempts to use an expired token, this handler is executed.

Response:

```json
{
    "error": "Token has expired"
}
```

Status:

```text
401 Unauthorized
```

---

# Revoked Token

```python
@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401
```

## Purpose

A revoked token is a token that has been explicitly invalidated by the server.

This project does not implement token revocation.

However, the handler is included for completeness and future extensibility.

Response:

```json
{
    "error": "Token has been revoked"
}
```

Status:

```text
401 Unauthorized
```

---

# Fresh Token Required

```python
@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401
```

## Purpose

Some applications distinguish between:

* regular tokens;
* fresh tokens.

A fresh token is typically issued immediately after login and may be required for sensitive operations such as changing a password.

This project does not use fresh tokens, but the handler demonstrates how Flask-JWT-Extended supports this feature.

Response:

```json
{
    "error": "Fresh token required"
}
```

Status:

```text
401 Unauthorized
```

---

# Why Return 401 Every Time?

The project specification requires that **all authentication errors** return the same HTTP status code.

Even though the causes are different, they all represent authentication failures.

Returning a consistent response makes the API predictable and satisfies the automated tests.

---

# Error Handling Workflow

```text
Client

↓

Protected Route

↓

@jwt_required()

↓

Validate Token

↓

┌───────────────────────────────┐
│ Missing Token                 │
│ Invalid Token                 │
│ Expired Token                 │
│ Revoked Token                 │
│ Fresh Token Required          │
└───────────────────────────────┘

↓

Corresponding Handler

↓

JSON Error Message

↓

401 Unauthorized
```

---

# Testing the Handlers

## Missing Token

```bash
curl http://127.0.0.1:5000/jwt-protected
```

Expected response:

```json
{
    "error": "Missing or invalid token"
}
```

---

## Invalid Token

```bash
curl http://127.0.0.1:5000/jwt-protected \
-H "Authorization: Bearer invalid_token"
```

Expected response:

```json
{
    "error": "Invalid token"
}
```

---

## Expired Token

An expired JWT automatically triggers:

```python
@jwt.expired_token_loader
```

Expected response:

```json
{
    "error": "Token has expired"
}
```

---

# Summary

JWT error handlers improve the API by:

* providing clear error messages;
* returning consistent HTTP responses;
* centralizing authentication error handling;
* preventing protected routes from executing when authentication fails.

These handlers make the API easier to maintain and ensure that authentication errors are handled in a predictable way.

---

📄 **Next file:** `06-role-based-access-control.md`
