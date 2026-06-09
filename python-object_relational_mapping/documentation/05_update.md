# UPDATE OBJECTS

## Retrieve an object

```python
state = session.query(State).filter(State.id == 1).first()
```

## Modify attributes

```python
state.name = "New Mexico"
```

## Save changes

```python
session.commit()
```