# LAB - Class 04

## Project: Garage Band with OOP
Overview: Creating a Garage Band with Object Oriented Programming.

## Author: Manuch Sadri

### Feature Tasks and Requirements

- Use Python classes to model a `Band` made up of different kinds of musicians.
- Start with `Guitarist`,`Bassist`, and `Drummer`.
- Make use of a `Musician` base class to handle common functionality which particular kinds of musicians will inherit.

### Testing Details

Unit tests will be supplied for this lab. Your job is to make them pass. Do NOT modify the supplied tests (except to enable for stretch goals.)

#### Band Tests
- A `Band` instance should have a `name` attribute which is a string.
- A `Band` instance should have a `members` attribute which is a list of instances that inherit from `Musician` base (or 
  super) class.
- A `Band` instance should have a `play_solos` method that asks each member musician to play a solo, in the order they 
  were added to band.
- A `Band` instance should have appropriate `__str__` and `__repr__` methods.
- A `Band` should have a class method `to_list` which returns a list of previously created `Band` instances

#### Musician Subclass Tests
- Each kind of `Musicia`n instance should have appropriate `__str__` and `__repr__` methods.
- Each kind of `Musician` instance should have a `get_instrument` method that returns string.
- Each kind of `Musician` instance should have a `play_solo` method that returns string.

#### Stretch
- See tests marked “stretch” in supplied test suite.
- Make Musician “abstract” - aka an Abstract Base Class
- Add your own tests.

---

#### Links and Resources
- back-end server url: n/a
- front-end application: n/a

#### Setup
.env requirements (where applicable)
- i.e.
  - PORT: n/a
  - DATABASE_URL: n/a

#### How to initialize/run your application (where applicable)

- set-up virtual env
  - \> ```python3.11 -m venv .venv```
  - \> ```source .venv/bin/activate```
  - \> ```pip install pytest```
- run cli app
  - \> ```doodah```
- run pytest
  - \> ```doodah```
- deactivate virtual env
  - \> ```deactivate```

#### How to use your library (where applicable)

- Tests
    - How do you run tests?
      - doodah
    - Any tests of note?
      - doodah
    - Describe any tests that you did not complete, skipped, etc
      - doodah