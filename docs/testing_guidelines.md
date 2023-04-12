# Testing guidelines

The tests need to follos the application pattern, what means, the test for the file:

> `app/mod_webhook/routes.py`

Needs to be inside of file:

> `tests/mod_webhook/routes_tests.py`

Every test needs to be inside a class with all the testing scenarios running
inside of methods inside the class.

For routes testing, the naming convention has to be the name `Test`, following with a name
of what is being tested and the method that is being tested, like:

> `TestMandrillGet` or `TestMandrillPost`

Inside, the methods need to follow the naming convention for every scenario, like
- Test success
- Test not found
- Test unauthorized
