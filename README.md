# WorkGenius Coding Challenge

## Requirements

- Python 3.10+
- virtualenv
- docker
- mongodb

## Local setup instructions:

### Using docker

To run the environment on docker you just need to execute
the command

> `docker compose up`

*Tip*: Use the argment -d to run the environment in background

### Debugging with pycharm

Generate the virtualenv with the command
> `python3 -m venv venv`

Enter on the virtual env
> `source venv/bin/activate`

Install the requirements
> `pip install -r requirements.txt`

To run the environment in a debug mode on pycharm,
first activate the mongodb docker image to connect to server

> `docker compose up pg`

*Tip*: you can use the `-d` flag to
rnn the mongodb server in background mode.
To shut down mongodb server in background,
just run `docker compose stop pg`

Then set up the `.env` using the `.env.example` file with the env vars needed to add the value
`postgresql://postgres:postgres@localhost:5434/db_wg` to `SQLALCHEMY_DATABASE_URI`
and debug the application on pycharm


Create all tables on database
> `flask db upgrade`

## Unit tests

To run the unit tests locally use the command:

> `pytest`

*Tip*: If you just want to run the tests that fails after a
full test, add the flag `--lf` and it will run only the failing tests.
If every test runs well, next time the pytest will execute all tests.

## Guidelines

Inside the `docs` directory, you will find the guidelines to make
- Tests
- Modules
- Handlers

It's recommended to follow these guidelines to ensure a consistent coding style across the project.
