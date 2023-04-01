from functools import wraps


class Api:
    def __init__(self):
        self.methods = {}

    def setup(self, messages):
        methods_list = [element for element in messages if
                        list(filter(lambda x: isinstance(x, dict), element))]

        for method in methods_list:
            fn = method[1]["function"]
            if not self.methods.get(f"{fn.__module__}.{fn.__name__}"):
                continue
            path = {"path": method[0] + method[1]["name"], "type": method[1]["type"]}
            self.methods[f"{fn.__module__}.{fn.__name__}"]["paths"].append(path)
            # print(json.dumps(self.methods, indent=4, ensure_ascii=True, default=lambda o: str(o)))

    def parameters(self, *args):

        def decorator(fn):
            self.methods[f"{fn.__module__}.{fn.__name__}"] = {"params_type": args, "paths": []}

            @wraps(fn)
            def wrapper(cls, request, *args, **kwargs):
                return fn(cls, request, *args, **kwargs)

            return wrapper

        return decorator
