# Database Connection

## Import Required Modules

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
```

---

## Create an Engine

```python
engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(user, password, database)
)
```

Creates an `Engine` object containing the information needed to communicate with the database:

* Database type (`mysql`)
* Driver (`mysqldb`)
* Username
* Password
* Host
* Port
* Database name

---

## Connection String Format

```python
"mysql+mysqldb://<username>:<password>@<host>:<port>/<database>"
```

Example:

```python
"mysql+mysqldb://root:mypassword@localhost:3306/hbtn_0e_6_usa"
```

---

## Lazy Connection

Calling:

```python
engine = create_engine(...)
```

does **not** immediately connect to MySQL.

SQLAlchemy simply prepares an `Engine` object. The actual connection is established only when the database needs to be accessed.

---

## Create a Session Factory

```python
Session = sessionmaker(bind=engine)
```

The session factory is linked to the engine and will use it to create sessions.

---

## Create a Session

```python
session = Session()
```

The session is used to interact with the database through the ORM.

---

## Execute a Query

```python
states = session.query(State).all()
```

When this query is executed:

1. SQLAlchemy requests a connection from the engine.
2. The engine opens a connection to MySQL.
3. The SQL query is sent.
4. Results are returned as Python objects.

---

## Typical Setup

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost:3306/{}"
    .format(user, password, database)
)

Session = sessionmaker(bind=engine)
session = Session()
```

---

## Connection Flow

```text
create_engine()
        ↓
Create an Engine object

sessionmaker(bind=engine)
        ↓
Create a Session factory

Session()
        ↓
Create a Session

session.query(...)
        ↓
Open a MySQL connection
        ↓
Execute SQL
        ↓
Return Python objects
```
