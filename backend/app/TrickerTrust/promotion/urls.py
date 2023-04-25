from django.urls import path

from promotion.views import PromotionViewSet

urlpatterns = [
    path("", PromotionViewSet.as_view({"get": "get_promotions",
                                       "post": "create_promotion",
                                       "delete": "delete_promotion"})),
    path("<int:pk>", PromotionViewSet.as_view({"put": "update_promotion"}))
]
