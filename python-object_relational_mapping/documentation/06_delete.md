# DELETE OBJECTS

## Retrieve an object

```python
state = session.query(State).filter(State.name == "Texas").first()
```

## Delete the object

```python
session.delete(state)
```

## Save changes

```python
session.commit()
```