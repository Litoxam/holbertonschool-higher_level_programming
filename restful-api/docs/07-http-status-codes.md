# HTTP Status Codes

HTTP status codes are returned by the server to indicate the result of an HTTP request.

Every response sent by the API includes a status code.

These codes allow the client to quickly determine whether a request was successful or if an error occurred.

This project mainly uses three status codes:

* **200 OK**
* **401 Unauthorized**
* **403 Forbidden**

---

# 200 OK

The **200 OK** status code indicates that the request was successfully processed.

The client requested a resource, and the server returned the expected response.

Example:

```http
GET /jwt-protected
Authorization: Bearer VALID_TOKEN
```

Response:

```text
JWT Auth: Access Granted
```

Status:

```text
200 OK
```

Another example:

```http
GET /admin-only
Authorization: Bearer ADMIN_TOKEN
```

Response:

```text
Admin Access: Granted
```

Status:

```text
200 OK
```

---

# 401 Unauthorized

The **401 Unauthorized** status code indicates that authentication has failed.

The server cannot verify the identity of the client.

This usually happens when:

* no credentials are provided;
* the username or password is incorrect;
* the JWT is missing;
* the JWT is invalid;
* the JWT has expired.

---

## Example — Missing Basic Authentication

Request:

```bash
curl http://127.0.0.1:5000/basic-protected
```

Response:

```text
401 Unauthorized
```

---

## Example — Wrong Password

Request:

```bash
curl -u user1:wrongpassword http://127.0.0.1:5000/basic-protected
```

Response:

```text
401 Unauthorized
```

---

## Example — Missing JWT

Request:

```bash
curl http://127.0.0.1:5000/jwt-protected
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

## Example — Invalid JWT

Request:

```bash
curl http://127.0.0.1:5000/jwt-protected \
-H "Authorization: Bearer invalid_token"
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

# 403 Forbidden

The **403 Forbidden** status code indicates that authentication succeeded, but the authenticated user is **not allowed** to access the requested resource.

Unlike **401**, the user's identity is already known.

The problem is not **who the user is**, but **what the user is allowed to do**.

---

## Example

A regular user authenticates successfully.

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{
    "username":"user1",
    "password":"password"
}'
```

The user receives a valid JWT.

The user then tries to access:

```bash
curl http://127.0.0.1:5000/admin-only \
-H "Authorization: Bearer USER_TOKEN"
```

Response:

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

# Comparing 401 and 403

These two status codes are frequently confused.

The difference is simple.

## 401 Unauthorized

The server cannot verify the client's identity.

Typical causes:

* missing credentials;
* incorrect credentials;
* invalid JWT;
* expired JWT.

Diagram:

```text
Client

↓

Authentication

↓

Failed

↓

401 Unauthorized
```

---

## 403 Forbidden

The server successfully authenticated the client.

However, the client does not have permission to access the requested resource.

Diagram:

```text
Client

↓

Authentication

↓

Successful

↓

Authorization

↓

Failed

↓

403 Forbidden
```

---

# Status Codes Used in This Project

| Status Code          | When it is Returned                                              |
| -------------------- | ---------------------------------------------------------------- |
| **200 OK**           | Authentication and authorization succeeded.                      |
| **401 Unauthorized** | Authentication failed or credentials are missing.                |
| **403 Forbidden**    | Authentication succeeded, but the user does not have permission. |

---

# Complete Request Flow

```text
Client Request

↓

Authentication

↓

Valid?

↓

No

↓

401 Unauthorized

──────────────

Yes

↓

Authorization

↓

Allowed?

↓

No

↓

403 Forbidden

──────────────

Yes

↓

200 OK
```

---

# Why Are Status Codes Important?

HTTP status codes provide a standard way for clients and servers to communicate.

Instead of analyzing the response body, a client can immediately determine whether a request succeeded simply by checking the status code.

For example:

* `200` means everything worked correctly.
* `401` means the client must authenticate.
* `403` means authentication succeeded, but access is not permitted.

Using the correct status codes makes an API easier to understand, easier to debug, and compliant with HTTP standards.

---

# Summary

This project uses three HTTP status codes to represent different outcomes:

* **200 OK** → The request succeeded.
* **401 Unauthorized** → Authentication failed.
* **403 Forbidden** → Authentication succeeded, but authorization failed.

Understanding the difference between these codes is essential when designing secure REST APIs.

---

📄 **Next file:** `08-api-testing.md`
