from collections import defaultdict
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.playground_core.params import required, result, error, description, Param, Types
from core.settings import PLAYGROUND_CORE
from playground_dev.constants import Error, Result, Params, Description


class Methods(ViewSet):
    @PLAYGROUND_CORE.parameters(
        description(text=Description.LIST_DESCRIPTION),
        result(description=Result.LIST_DESCRIPTION, objects=Result.LIST_OBJECT, code=200)
    )
    def methods_list(self, request):
        method_categories = defaultdict(list)
        for method in PLAYGROUND_CORE.methods.keys():
            method_categories[method.split(".")[0]].append(method)

        return Response(dict(method_categories))

    @PLAYGROUND_CORE.parameters(
        description(text=Description.RETRIEVE_DESCRIPTION),
        required(name="method", param_type=Param.PARAM, description=Params.RETRIEVE_DESCRIPTION, name_type=Types.STR),
        result(description=Result.RETRIEVE_DESCRIPTION, objects=Result.RETRIEVE_OBJECT, code=200),
        error(code=404, description=Error.METHOD_NOT_FOUND),
    )
    def method_retrieve(self, request, method: str) -> Response:
        django_method = PLAYGROUND_CORE.methods.get(method)

        if not django_method:
            return Response({"error": Error.METHOD_NOT_FOUND}, status=404)

        return Response(django_method)
