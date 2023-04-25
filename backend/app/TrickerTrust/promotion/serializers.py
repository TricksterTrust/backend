from rest_framework import serializers

from promotion.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = "__all__"

    def create(self, validated_data):
        if validated_data["primary"] is True:
            Promotion.objects.filter(primary=True).delete()

        return super().create(validated_data)
