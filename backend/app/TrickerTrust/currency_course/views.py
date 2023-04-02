from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from core.playground_core.params import description, result
from core.settings import PLAYGROUND_CORE
from currency_course.models import Currency
from currency_course.serializers import CurrencySerializer


class CurrencyViewSet(ViewSet):
    @PLAYGROUND_CORE.parameters(
        description(text="Позволяет получить список всех валют",
                    warning_text="Все валюты указаны в рублях"),
        result(description="Возвращает список объектов.",
               objects={"currencies": []},
               code=200)
    )
    def get_currencies(self, request: Request):
        currencies = CurrencySerializer(Currency.objects.order_by("primary").all(), many=True)
        return Response(currencies.data)
