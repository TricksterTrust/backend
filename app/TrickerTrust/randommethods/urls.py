from django.urls import path

from randommethods import views

urlpatterns = [
    path("random2/", views.Methods1.as_view({"get": "list"}))
]