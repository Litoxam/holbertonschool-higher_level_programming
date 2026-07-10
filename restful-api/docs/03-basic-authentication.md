# Basic Authentication

This document explains how **HTTP Basic Authentication** is implemented in this project.

Basic Authentication is the first layer of security used by the API before introducing JWT authentication.

---

# What is Basic Authentication?

Basic Authentication is an HTTP authentication method.

Instead of requesting a token, the client sends its **username** and **password** with every request.

Those credentials are transmitted inside the HTTP `Authorization` header.

Example:

```http
GET /basic-protected
Authorization: Basic dXNlcjE6cGFzc3dvcmQ=
```

The value after `Basic` is a Base64-encoded string representing:

```text
username:password
```

For example:

```text
user1:password
```

becomes:

```text
dXNlcjE6cGFzc3dvcmQ=
```

> **Important**
>
> Base64 is **not encryption**.
> It is simply an encoding format.
> Anyone can decode it.
>
> For this reason, Basic Authentication should always be used over **HTTPS**.

---

# Creating the Authentication Manager

The authentication manager is initialized with:

```python
auth = HTTPBasicAuth()
```

This object is responsible for:

* reading the `Authorization` header;
* extracting the username and password;
* calling the verification function;
* returning an authentication error if needed.

Without this object, Flask would not know how to authenticate users.

---

# Verifying Credentials

The verification function tells Flask how to validate a username and password.

```python
@auth.verify_password
def verify_password(username, password):
    # Find the user in memory
    user = users.get(username)

    # Check user and password
    if user and check_password_hash(user["password"], password):
        return username

    return None
```

The decorator:

```python
@auth.verify_password
```

registers this function inside Flask-HTTPAuth.

The function is **never called manually**.

Whenever a protected endpoint receives a request, Flask-HTTPAuth automatically executes it.

---

# Step 1 — Retrieve the User

```python
user = users.get(username)
```

The username received from the client is searched inside the user dictionary.

If the username exists:

```python
user = {
    "username": "user1",
    "password": "...",
    "role": "user"
}
```

Otherwise:

```python
user = None
```

---

# Step 2 — Verify the Password

```python
check_password_hash(user["password"], password)
```

The stored password is already hashed.

The password received from the client is plain text.

`check_password_hash()` hashes the entered password and compares it with the stored hash.

Result:

```text
True
```

or

```text
False
```

This allows passwords to be verified without ever storing them in plain text.

---

# Step 3 — Return the Result

If authentication succeeds:

```python
return username
```

Returning any non-empty value tells Flask-HTTPAuth that authentication was successful.

If authentication fails:

```python
return None
```

Flask-HTTPAuth automatically returns:

```text
401 Unauthorized
```

No additional code is required.

---

# Protecting an Endpoint

The endpoint is protected with:

```python
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def get_basic():
    return "Basic Auth: Access Granted"
```

The decorator:

```python
@auth.login_required
```

executes **before** the route function.

Its job is to verify the client's credentials.

If authentication succeeds:

```
get_basic()
```

is executed.

Otherwise, Flask immediately returns:

```text
401 Unauthorized
```

---

# Authentication Flow

```
Client

GET /basic-protected

↓

Authorization Header

↓

Flask-HTTPAuth

↓

verify_password()

↓

User exists?

↓

Password correct?

↓

Yes

↓

Execute Route

↓

Basic Auth: Access Granted
```

---

# Testing the Endpoint

## Request Without Credentials

```bash
curl http://127.0.0.1:5000/basic-protected
```

Response:

```text
401 Unauthorized
```

---

## Request With Valid Credentials

```bash
curl -u user1:password http://127.0.0.1:5000/basic-protected
```

Response:

```text
Basic Auth: Access Granted
```

HTTP Status:

```text
200 OK
```

---

## Request With Invalid Credentials

```bash
curl -u user1:wrongpassword http://127.0.0.1:5000/basic-protected
```

Response:

```text
401 Unauthorized
```

---

# Why Hash Passwords?

Suppose passwords were stored like this:

```python
users = {
    "user1": {
        "password": "password"
    }
}
```

If the application were compromised, every password would be immediately exposed.

Instead, passwords are stored as hashes:

```python
users = {
    "user1": {
        "password": "scrypt:32768:8:1$..."
    }
}
```

Even if someone gains access to the data, the original password is not directly visible.

This is why password hashing is considered a security best practice.

---

# Advantages

* Simple to implement.
* Built into the HTTP protocol.
* Supported by most HTTP clients.
* Ideal for learning authentication concepts.

---

# Limitations

Basic Authentication requires sending the username and password with **every request**.

Although HTTPS encrypts network traffic, repeatedly sending credentials is not ideal.

Modern APIs generally authenticate users once, then issue a token.

This approach is implemented using **JSON Web Tokens (JWT)** in the next section.

---

# Summary

Basic Authentication introduced several important concepts:

* HTTP Authorization headers
* Credential verification
* Password hashing
* Protected routes
* Authentication decorators
* HTTP status code **401 Unauthorized**

The next document explains how JWT authentication improves this workflow by replacing repeated username/password exchanges with secure access tokens.

📄 **Next file:** `04-jwt-authentication.md`
