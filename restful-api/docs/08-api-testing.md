# API Testing

Testing is an essential part of API development.

It ensures that every endpoint behaves as expected and returns the correct responses under different conditions.

Throughout this project, the API is tested using **curl** from the command line.

---

# Why Test an API?

Testing allows developers to verify that:

* endpoints are reachable;
* authentication works correctly;
* responses match the project specifications;
* HTTP status codes are correct;
* errors are properly handled.

Without testing, it is impossible to know whether an API behaves as intended.

---

# Starting the Server

Before testing any endpoint, start the Flask application.

```bash
python3 task_05_basic_security.py
```

Expected output:

```text
 * Serving Flask app 'task_05_basic_security'
 * Running on http://127.0.0.1:5000
```

The API is now ready to receive requests.

---

# Testing Basic Authentication

## Without Credentials

Request:

```bash
curl http://127.0.0.1:5000/basic-protected
```

Expected response:

```text
401 Unauthorized
```

This confirms that the endpoint is correctly protected.

---

## With Valid Credentials

Request:

```bash
curl -u user1:password http://127.0.0.1:5000/basic-protected
```

Expected response:

```text
Basic Auth: Access Granted
```

Status:

```text
200 OK
```

---

## With Invalid Credentials

Request:

```bash
curl -u user1:wrongpassword http://127.0.0.1:5000/basic-protected
```

Expected response:

```text
401 Unauthorized
```

---

# Testing the Login Endpoint

The `/login` endpoint authenticates a user and returns a JWT.

Request:

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{
    "username":"user1",
    "password":"password"
}'
```

Expected response:

```json
{
    "access_token": "eyJhbGc..."
}
```

The returned JWT will be used for every protected endpoint.

---

# Saving the JWT

Instead of copying the token manually, it can be stored inside a shell variable.

```bash
TOKEN=$(curl -s -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username":"user1","password":"password"}' | jq -r .access_token)
```

The variable can then be reused for every request.

---

# Testing JWT Authentication

## Valid Token

Request:

```bash
curl http://127.0.0.1:5000/jwt-protected \
-H "Authorization: Bearer $TOKEN"
```

Expected response:

```text
JWT Auth: Access Granted
```

Status:

```text
200 OK
```

---

## Missing Token

Request:

```bash
curl http://127.0.0.1:5000/jwt-protected
```

Expected response:

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

## Invalid Token

Request:

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

Status:

```text
401 Unauthorized
```

---

# Testing Role-Based Access Control

## Login as a Regular User

```bash
USER_TOKEN=$(curl -s -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username":"user1","password":"password"}' | jq -r .access_token)
```

Attempt to access the administrator endpoint.

```bash
curl http://127.0.0.1:5000/admin-only \
-H "Authorization: Bearer $USER_TOKEN"
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
ADMIN_TOKEN=$(curl -s -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username":"admin1","password":"password"}' | jq -r .access_token)
```

Access the administrator endpoint.

```bash
curl http://127.0.0.1:5000/admin-only \
-H "Authorization: Bearer $ADMIN_TOKEN"
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

# Common Testing Workflow

During development, a typical testing sequence is:

```text
Start Flask Server

↓

Test Basic Authentication

↓

Test Login

↓

Retrieve JWT

↓

Test JWT-Protected Route

↓

Test Admin Route

↓

Verify Error Responses
```

This ensures that every feature works before moving on to the next one.

---

# Why Use curl?

`curl` is one of the most popular command-line tools for testing APIs.

Advantages include:

* available on most operating systems;
* lightweight;
* supports every HTTP method;
* allows custom headers;
* easy to integrate into scripts.

Although tools such as Postman or Insomnia provide graphical interfaces, `curl` remains an excellent choice for learning HTTP and understanding exactly what is sent to the server.

---

# Summary

Testing should be performed after every modification to ensure that:

* routes are reachable;
* authentication behaves correctly;
* authorization is enforced;
* error handlers return the expected responses;
* HTTP status codes comply with the project specifications.

Systematic testing helps identify problems early and ensures that the API remains reliable as new features are added.

---

📄 **Next file:** `09-concepts-learned.md`
