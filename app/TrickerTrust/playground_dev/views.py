import inspect
from typing import Any, List

from django.http import HttpResponse
from django.urls import URLPattern, URLResolver
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from TrickerTrust.playground_core.get_urls import required, optional, result, description, error
from TrickerTrust.settings import PLAYGROUND_CORE
from playground_dev.messages import Message


def list_urls(lis, acc=None):
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


def parameters(*args):
    print(args)

    def decorator(fn):
        def wrapper(self, request):
            return fn(self, request)

        return wrapper

    return decorator


class Methods(ViewSet):
    @PLAYGROUND_CORE.parameters()
    def methods_list(self, request):
        methods = {}
        for method in PLAYGROUND_CORE.methods.keys():
            method_category = method.split(".")[0]
            if method_category not in methods:
                methods[method_category] = []

            methods[method_category].append(method)
        return Response(methods)

    @PLAYGROUND_CORE.parameters(
        required(name="method", param_type="query", description="Нужный метод для выдачи информации", name_type="str"),
        result(description="Возвращает всю доступную информацию о методе", objects={"params_type": List, "paths": List},
               code=200),
        error(code=404, description="Метод не найден")
    )
    def method_retrieve(self, request, method: str):
        if method not in PLAYGROUND_CORE.methods.keys():
            return Response({"error": Message.METHOD_NOT_FOUND})

        for method_key, method_value in PLAYGROUND_CORE.methods.items():
            if method_key == method:
                return Response(method_value)

        return Response(method)
