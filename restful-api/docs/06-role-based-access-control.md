# Role-Based Access Control (RBAC)

This document explains how **Role-Based Access Control (RBAC)** is implemented in the project.

Authentication confirms **who the user is**.

Authorization determines **what the user is allowed to do**.

The `/admin-only` endpoint demonstrates this concept by allowing access only to users with the `admin` role.

---

# What is RBAC?

RBAC stands for **Role-Based Access Control**.

Instead of giving every authenticated user the same permissions, access is granted according to a user's role.

In this project, two roles exist:

| Role    | Permissions                                                        |
| ------- | ------------------------------------------------------------------ |
| `user`  | Access to authenticated endpoints                                  |
| `admin` | Access to authenticated endpoints and administrator-only endpoints |

---

# Authentication vs Authorization

These two concepts are often confused, but they solve different problems.

## Authentication

Authentication answers the question:

> **Who are you?**

Example:

```text
Username: user1
Password: password
```

or

```text
Bearer eyJhbGc...
```

If the credentials or token are valid:

```text
200 OK
```

Otherwise:

```text
401 Unauthorized
```

---

## Authorization

Authorization answers the question:

> **What are you allowed to do?**

An authenticated user may still be denied access if they do not have the required permissions.

Example:

```text
Authenticated User

↓

Role = user

↓

GET /admin-only

↓

403 Forbidden
```

---

# Protecting the Route

The administrator endpoint is defined as:

```python
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def get_admin_only():
```

The first layer of protection is:

```python
@jwt_required()
```

Before the function executes, Flask verifies:

* that a JWT exists;
* that it is valid;
* that it has not expired.

Only authenticated users can reach the rest of the function.

---

# Step 1 — Retrieve the User Identity

```python
current_user = get_jwt_identity()
```

When the JWT was created, the username was stored inside the token.

Example:

```python
create_access_token(identity="user1")
```

Later:

```python
get_jwt_identity()
```

returns:

```text
user1
```

or

```text
admin1
```

depending on who logged in.

---

# Step 2 — Retrieve the User

```python
user = users.get(current_user)
```

The username returned by the JWT is used to retrieve the user's information.

Example:

```python
{
    "username": "admin1",
    "password": "...",
    "role": "admin"
}
```

The application now knows everything it needs about the authenticated user.

---

# Step 3 — Check the Role

```python
if user["role"] != "admin":
    return jsonify({
        "error": "Admin access required"
    }), 403
```

This is the authorization step.

If the user's role is not `"admin"`:

* the request is rejected;
* the route immediately returns a `403 Forbidden`.

If the role is `"admin"`:

the request continues.

---

# Step 4 — Grant Access

If every check succeeds:

```python
return "Admin Access: Granted"
```

The client receives:

```text
Admin Access: Granted
```

Status:

```text
200 OK
```

---

# Complete Authorization Flow

```text
Client

↓

GET /admin-only

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

users.get(current_user)

↓

Role == "admin" ?

↓

No

↓

403 Forbidden

──────────────

Yes

↓

Execute Route

↓

Admin Access: Granted
```

---

# Why Return 403?

The request is **not rejected because of authentication**.

The user has already been authenticated successfully.

The request is rejected because the authenticated user does not have sufficient permissions.

That is exactly what **403 Forbidden** means.

| Status Code          | Meaning                                         |
| -------------------- | ----------------------------------------------- |
| **401 Unauthorized** | Authentication failed.                          |
| **403 Forbidden**    | Authentication succeeded, but access is denied. |

---

# Testing the Endpoint

## Login as a Regular User

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{
    "username":"user1",
    "password":"password"
}'
```

Copy the returned token.

Then:

```bash
curl http://127.0.0.1:5000/admin-only \
-H "Authorization: Bearer YOUR_TOKEN"
```

Expected response:

```json
{
    "error": "Admin access required"
}
```

Status:

```text
403 Forbidden
```

---

## Login as an Administrator

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{
    "username":"admin1",
    "password":"password"
}'
```

Copy the returned token.

Then:

```bash
curl http://127.0.0.1:5000/admin-only \
-H "Authorization: Bearer YOUR_ADMIN_TOKEN"
```

Expected response:

```text
Admin Access: Granted
```

Status:

```text
200 OK
```

---

# Why Use RBAC?

Role-Based Access Control provides several benefits:

* prevents unauthorized access to sensitive resources;
* separates users according to their permissions;
* makes the application easier to maintain;
* allows new roles to be added without changing the authentication system.

RBAC is one of the most common authorization models used in modern web applications.

---

# Summary

Role-Based Access Control introduced several important concepts:

* Authentication and Authorization are different.
* A valid JWT does not automatically grant every permission.
* User roles determine which resources can be accessed.
* `403 Forbidden` indicates insufficient permissions.
* RBAC makes applications more secure and easier to scale.

---

📄 **Next file:** `07-http-status-codes.md`
