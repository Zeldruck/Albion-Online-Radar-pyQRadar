import importlib
from os import scandir


class Routes:
    """A class for dynamically registering blueprints from route modules."""

    def __new__(cls, app):
        """
        Dynamically register blueprints from route modules.

        Parameters:
        - app (Flask): The Flask application instance.

        Returns:
        - Map: The Flask application's URL map.
        """
        route_folder = "pyqradar/routes"

        for item in scandir(route_folder):
            if (
                item.is_file()
                and "routes" not in item.name
                and "__init__" not in item.name
                and item.name.endswith(".py")
            ):
                module_name = item.name.removesuffix(".py")
                importlib.import_module(f"pyqradar.routes.{module_name}")

        return app.url_map
