# Python - Object Relational Mapping

This project explores the interaction between Python and MySQL databases using both **MySQLdb** and **SQLAlchemy**.

## Learning Objectives

At the end of this project, I am expected to be able to explain:

* How to connect Python to a MySQL database.
* How to execute SQL queries from Python.
* How to fetch and manipulate query results.
* How to prevent SQL injection.
* What an ORM is and why it is useful.
* The difference between MySQLdb and SQLAlchemy.
* How to map Python classes to database tables.
* How to create, read, update and delete records using SQLAlchemy.

## Requirements

* Ubuntu 20.04 LTS
* Python 3.8.5
* MySQLdb 2.0.x
* SQLAlchemy 1.4.x
* pycodestyle 2.7.*

## Technologies

* Python
* MySQL
* MySQLdb
* SQLAlchemy
* Object Relational Mapping (ORM)

## Project Structure

| File                            | Description                                         |
| ------------------------------- | --------------------------------------------------- |
| [0-select_states.py](./0-select_states.py)           | Lists all states from the database.                 |
| [1-filter_states.py](./1-filter_states.py) | Lists states starting with `N`. |
| [2-my_filter_states.py](./2-my_filter_states.py) | Filters states according to user input. |
| [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | Prevents SQL injection using parameterized queries.            |
| [4-cities_by_state.py](./4-cities_by_state.py) | Lists all cities with their corresponding states. |
| [5-filter_cities.py](./5-filter_cities.py) | Lists cities belonging to a given state. |
| [model_state.py](./model_state.py) | Defines the State class using SQLAlchemy. |
| [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Lists all State objects. |
| [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Displays the first State object. |
| [9-model_state_filter_a.py](./9-model_state_filter_a.py) | Lists states containing the letter `a`. |
| [10-model_state_my_get.py](./10-model_state_my_get.py) | Retrieves a state by name. |
| [11-model_state_insert.py](./11-model_state_insert.py) | Inserts a new State object. |
| [12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | Updates the State object with id `2`. |
| [13-model_state_delete_a.py](./13-model_state_delete_a.py) | Deletes states containing the letter `a`. |


## Author

**Maxime Bernier**
