from django.urls import URLPattern, URLResolver


def list_urls(urlpatterns: list = None, returned: list = None):
    if returned is None:
        returned = []

    if not urlpatterns:
        return

    urlconf = urlpatterns[0]
    if isinstance(urlconf, URLPattern):
        if hasattr(urlconf.callback, "actions"):
            for action_method, action in urlconf.callback.actions.items():
                if not hasattr(urlconf.callback.cls, action):
                    continue

                yield returned + [{"name": str(urlconf.pattern),
                                   "type": action_method,
                                   "function": getattr(urlconf.callback.cls, action),
                                   "authorization": getattr(urlconf.callback.cls, "permission_classes")}]
        else:
            yield returned + [str(urlconf.pattern)]

    elif isinstance(urlconf, URLResolver):
        yield from list_urls(urlconf.url_patterns, returned + [str(urlconf.pattern)])

    yield from list_urls(urlpatterns[1:], returned)
