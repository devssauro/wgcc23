# Module guidelines

When creating a new module for your Flask application, follow these guidelines:

- The module should be defined in a Python package named routes. This package should contain all of your Flask routes.
- The file name for the route should be the same as the name of the route, but with underscores instead of hyphens.
For example, if the module is `webhook`, the package should be `mod_webhook`.
- If only a single set of routes will be made on module, all routes must has to be on `routes.py`
- If more groups of routes has to be in the same module, such as more webhooks for more platforms,
the routes must have to be a package and each group of routes has to be inside of that package
- Every group of route have to belong to a blueprint to be registered on
the global blueprint for the module
- All blueprints (from `routes.py` or from `routes package`) have to be registered on blueprint
inside of `__init__.py` for the module, and it's blueprint has to be registered on application

By following these guidelines, you can create well-organized, maintainable, and easily understandable modules
for your Flask application.
