from django.urls import path

from currency_course import views

urlpatterns = [
    path("currency_rates/", views.CurrencyViewSet.as_view({"get": "get_currencies"})),
    path("exchange/", views.CurrencyViewSet.as_view({"post": "exchange_currencies"}))
]