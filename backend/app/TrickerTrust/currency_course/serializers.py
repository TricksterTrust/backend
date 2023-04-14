from rest_framework import serializers

from currency_course.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ["flag", "value", "code"]


class ExchangeSerializer(serializers.Serializer):
    to_code = serializers.CharField(max_length=10)
    from_code = serializers.CharField(max_length=10)
    value = serializers.FloatField(max_value=1_000_000, min_value=1, default=1)




