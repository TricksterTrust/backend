from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.playground_core.params import description, result, required, Types, Param, optional
from core.settings import PLAYGROUND_CORE
from currency_course.constants import Description, Result, Params, Error
from currency_course.models import Currency
from currency_course.serializers import CurrencySerializer, ExchangeSerializer


class CurrencyViewSet(ViewSet):
    @PLAYGROUND_CORE.parameters(
        description(text=Description.CURRENCY_DESCRIPTION, warning_text=Description.CURRENCY_WARNING),
        result(description=Result.CURRENCY_DESCRIPTION, objects=Result.CURRENCY_OBJECT, code=200)
    )
    def get_currencies(self, request: Request):
        currencies = CurrencySerializer(Currency.objects.order_by("primary", "id").all(), many=True)
        return Response(currencies.data)

    @PLAYGROUND_CORE.parameters(
        description(text=Description.EXCHANGE_DESCRIPTION),
        required(name="to_code", name_type=Types.STR, param_type=Param.BODY, description=Params.CODE_TO_DESCRIPTION),
        required(name="from_code", name_type=Types.STR, param_type=Param.BODY, description=Params.CODE_FROM_DESC),
        optional(name="value", name_type=Types.FLOAT, param_type=Param.BODY, description=Params.VALUE_DESCRIPTION,
                 warning_description=Params.VALUE_WARNING),
        result(description=Result.EXCHANGE_DESCRIPTION, objects=Result.EXCHANGE_OBJECT, code=200)
    )
    def exchange_currencies(self, request: Request):
        currencies = ExchangeSerializer(data=request.data)
        currencies.is_valid(raise_exception=True)
        body = currencies.validated_data
        currencies = Currency.objects.filter(code__in=[body["to_code"], body["from_code"]])

        if currencies.count() != 2:
            raise ValidationError({"detail": Error.CODE_NOT_FOUND})

        values = list(sorted(currencies.values("value", "code"), key=lambda x: x["code"] != body["to_code"]))
        exchange_rate = values[0]["value"] / values[1]["value"]
        return Response({"value": exchange_rate * body["value"]})