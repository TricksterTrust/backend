import sys
from typing import Any, Union

from django.urls import URLPattern, URLResolver


def list_urls(lis=None, acc=None):
    if acc is None:
        acc = []

    if not lis:
        return
    l = lis[0]
    if isinstance(l, URLPattern):
        if hasattr(l.callback, "actions"):
            for action_method, action in l.callback.actions.items():
                if not hasattr(l.callback.cls, action):
                    continue

                yield acc + [{"name": str(l.pattern),
                              "type": action_method,
                              "function": getattr(l.callback.cls, action)}]
                # print(l.callback.cls[action])
        else:
            yield acc + [str(l.pattern)]

    elif isinstance(l, URLResolver):
        yield from list_urls(l.url_patterns, acc + [str(l.pattern)])

    yield from list_urls(lis[1:], acc)


def required(name: str,
             name_type: str,
             param_type: str = "query",
             description: str = "",
             warning_description: str = "") -> dict:
    return {"name": name,
            "type": "required",
            "param_type": param_type,
            "description": description,
            "name_type": name_type,
            "warning_description": warning_description}


def optional(name: str,
             name_type: str,
             default: Any = None,
             param_type: str = "query",
             description: str = "",
             warning_description: str = "") -> dict:
    return {"name": name,
            "default": default,
            "type": "optional",
            "param_type": param_type,
            "description": description,
            "name_type": name_type,
            "warning_description": warning_description}


def description(text: str = "", warning_text: str = ""):
    return {"type": "description",
            "text": text,
            "warning_text": warning_text}


def error(code: int, description: str):
    return {"type": "errors",
            "code": code,
            "description": description}


def result(description: str = "", objects: Union[dict, list, None, str] = None, code: int = 200):
    return {"type": "result",
            "description": description,
            "objects": str(objects),
            "code": code}
