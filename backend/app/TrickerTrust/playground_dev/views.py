from collections import defaultdict

from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.playground_core.params import required, result, error, description
from core.settings import PLAYGROUND_CORE
from playground_dev.constants import Error, Result, Params, Description, Param, Types


class Methods(ViewSet):
    @PLAYGROUND_CORE.parameters(
        description(text=Description.LIST_DESCRIPTION,
                    warning_text=Description.LIST_WARNING),
        result(description=Result.LIST_DESCRIPTION,
               objects={'category': [str, str], "category_1": [str]},
               code=200)
    )
    def methods_list(self, request):
        method_categories = defaultdict(list)
        for method in PLAYGROUND_CORE.methods.keys():
            method_categories[method.split(".")[0]].append(method)

        return Response(dict(method_categories))

    @PLAYGROUND_CORE.parameters(
        description(text=Description.RETRIEVE_DESCRIPTION,
                    warning_text=Description.RETRIEVE_WARNING),
        required(name="method",
                 param_type=Param.PARAM,
                 description=Params.RETRIEVE_DESCRIPTION,
                 warning_description=Params.RETRIEVE_WARNING,
                 name_type=Types.STRING),
        result(description=Result.RETRIEVE_DESCRIPTION,
               objects={"params_type": [], "paths": []},
               code=200),
        error(code=404,
              description=Error.METHOD_NOT_FOUND)
    )
    def method_retrieve(self, request, method: str) -> Response:
        django_method = PLAYGROUND_CORE.methods.get(method)
        if not django_method:
            return Response({"error": Error.METHOD_NOT_FOUND}, status=404)

        return Response(django_method)

