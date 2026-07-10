# Flask Basics

This document explains the foundations of the Flask application used in this project.

Before implementing authentication or creating API endpoints, several components must be initialized.

---

# What is Flask?

Flask is a lightweight Python web framework used to build web applications and REST APIs.

Instead of manually creating an HTTP server, Flask provides tools to:

* create an application
* define routes
* receive HTTP requests
* send HTTP responses
* organize application logic

A Flask application starts by importing the required modules.

```python
from flask import Flask, request, jsonify
```

---

# The Flask Class

```python
from flask import Flask
```

`Flask` is the main class of the framework.

It creates the application that will receive HTTP requests and send HTTP responses.

The application is created with:

```python
app = Flask(__name__)
```

### Why `__name__`?

`__name__` tells Flask where the application is located.

It allows Flask to correctly load:

* configuration files
* templates
* static files

Every Flask application starts this way.

---

# The Request Object

```python
from flask import request
```

The `request` object contains everything sent by the client.

For example, if a client sends:

```http
POST /login
Content-Type: application/json
```

Body:

```json
{
    "username": "user1",
    "password": "password"
}
```

The JSON body can be retrieved with:

```python
data = request.get_json()
```

Result:

```python
{
    "username": "user1",
    "password": "password"
}
```

This allows the API to access the values sent by the client.

---

# The jsonify() Function

```python
from flask import jsonify
```

`jsonify()` converts Python dictionaries into JSON responses.

Example:

```python
return jsonify({
    "message": "Hello World"
})
```

Response:

```json
{
    "message": "Hello World"
}
```

Unlike returning a dictionary directly, `jsonify()` automatically:

* converts the dictionary into JSON
* sets the correct `Content-Type`
* creates a valid HTTP response

---

# Basic Authentication

```python
from flask_httpauth import HTTPBasicAuth
```

This project uses **Flask-HTTPAuth** to simplify Basic Authentication.

Instead of manually reading the `Authorization` header, Flask-HTTPAuth automatically:

* extracts the username
* extracts the password
* calls the verification function
* returns a response if authentication fails

The authentication manager is created with:

```python
auth = HTTPBasicAuth()
```

This object will later be used with:

```python
@auth.verify_password
```

and

```python
@auth.login_required
```

---

# Password Security

```python
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
```

Passwords should never be stored as plain text.

Instead of saving:

```text
password
```

the application stores a secure hash.

Example:

```python
generate_password_hash("password")
```

Result:

```text
scrypt:32768:8:1$...
```

When the user logs in, the password is verified with:

```python
check_password_hash(stored_hash, password)
```

This function returns:

```text
True
```

or

```text
False
```

without revealing the original password.

---

# JWT Authentication

```python
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
```

Flask-JWT-Extended provides all the tools needed to implement JWT authentication.

Each imported function has a specific role.

---

## JWTManager

```python
JWTManager
```

Initializes JWT support inside the Flask application.

Example:

```python
jwt = JWTManager(app)
```

---

## create_access_token()

Creates a signed JWT after a successful login.

Example:

```python
token = create_access_token(identity=username)
```

The returned token is sent back to the client.

---

## jwt_required()

Protects an endpoint by requiring a valid JWT.

Example:

```python
@jwt_required()
```

Before executing the route, Flask automatically checks:

* if a token exists
* if the signature is valid
* if the token has expired

If one of these checks fails, access is denied.

---

## get_jwt_identity()

Retrieves the identity stored inside a JWT.

Example:

```python
current_user = get_jwt_identity()
```

If the token was created with:

```python
create_access_token(identity="user1")
```

then:

```python
get_jwt_identity()
```

returns:

```text
user1
```

---

# Creating the Flask Application

The application is initialized with:

```python
app = Flask(__name__)
```

This object represents the API.

Every route created later will belong to this application.

---

# Configuring the Secret Key

```python
app.config["JWT_SECRET_KEY"] = "your_secret_key"
```

The secret key is one of the most important parts of JWT authentication.

It is used to:

* sign JWT tokens
* verify JWT signatures

Without the correct secret key, fake tokens cannot be validated.

For security reasons, this key should always remain private.

In production, it should be long, random, and stored in an environment variable rather than directly in the source code.

---

# Initializing JWT

Once the secret key is configured, JWT support is enabled.

```python
jwt = JWTManager(app)
```

This connects Flask with Flask-JWT-Extended.

Without this initialization:

* JWT tokens cannot be generated.
* `@jwt_required()` cannot protect routes.
* JWT error handlers cannot be used.

---

# Creating the User Database

This project does not use MySQL or another database.

Instead, users are stored inside a Python dictionary.

Example:

```python
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}
```

Each user contains:

* a username
* a hashed password
* a role

The role determines which protected resources the user can access later.

Although this approach is not suitable for production, it is ideal for learning authentication concepts without introducing database complexity.

---

# Summary

At this point, the application has:

* created the Flask application;
* initialized Basic Authentication;
* initialized JWT authentication;
* configured the JWT secret key;
* created an in-memory user database.

The next step is to learn how Basic Authentication works and how the first protected endpoint is implemented.

📄 **Next file:** `03-basic-authentication.md`
