from functools import wraps

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request


class Api:
    def __init__(self):
        self.methods: dict = {}

    def setup(self, messages):
        methods_list: list = [element for element in messages if list(filter(lambda x: isinstance(x, dict), element))]

        for root_path, method in methods_list:
            fn = method["function"]
            method_name: str = f"{fn.__module__.replace('.views', '')}.{fn.__name__}"

            if method_name not in self.methods:
                continue

            auth = method.get('authorization') or fn.permission_classes
            isauth = (auth and issubclass(auth[0], IsAuthenticated))

            path: dict = {"path": f"{root_path}{method['name']}", "type": method["type"], "authenticated": isauth}
            self.methods[method_name]["paths"].append(path)

    def parameters(self, *params):

        def decorator(fn):
            method_name: str = f"{fn.__module__.replace('.views', '')}.{fn.__name__}"
            self.methods[method_name] = {"params_type": params, "paths": []}

            @wraps(fn)
            def wrapper(cls, request: Request, *args, **kwargs):
                return fn(cls, request, *args, **kwargs)

            return wrapper

        return decorator
