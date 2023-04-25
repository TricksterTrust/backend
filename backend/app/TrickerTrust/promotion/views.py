from rest_framework.viewsets import ModelViewSet

from core.playground_core.params import description, optional, Types, required, result
from core.settings import PLAYGROUND_CORE
from promotion.models import Promotion
from promotion.permissions import PromotionPermission
from promotion.serializers import PromotionSerializer


class PromotionViewSet(ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    permission_classes = [PromotionPermission]

    def get_queryset(self):
        primary = self.request.query_params.get("primary")
        if primary:
            return self.queryset.filter(primary=primary.lower() == "true")

        return self.queryset

    @PLAYGROUND_CORE.parameters(
        description(text="Отдаёт список проходящих акций",
                    warning_text="Создание\\удаление\\изменение только с авторизацией!"),
        required(name="description", name_type=Types.STR, description="Текст акции"),
        optional(name="url", name_type=Types.STR, description="Ссылка для перехода на страницу акции"),
        optional(name="end_time", name_type=Types.DATETIME, description="Время окончания акции"),
        optional(name="primary", name_type=Types.BOOL, description="Главная акция", default="false",
                 warning_description="При создании новой главной акции - старая удаляется"),
        result(description="Список с акциями", objects=["Object[Promo]"], code=200)
    )
    def get_promotions(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @PLAYGROUND_CORE.parameters()
    def create_promotion(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @PLAYGROUND_CORE.parameters()
    def update_promotion(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @PLAYGROUND_CORE.parameters()
    def delete_promotion(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
