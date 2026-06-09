# Common CRUD Operations

## Create

```python
new_state = State(name="Louisiana")
session.add(new_state)
session.commit()
```

## Read

```python
session.query(State).all()
session.query(State).first()
session.query(State).filter(State.name == "Texas").first()
session.query(State).order_by(State.id).all()
```

## Update

```python
state = session.query(State).filter(State.id == 1).first()
state.name = "New Mexico"
session.commit()
```

## Delete

```python
state = session.query(State).filter(State.id == 1).first()
session.delete(state)
session.commit()
```

## Close the session

```python
session.close()
```