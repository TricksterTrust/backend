from django.urls import path
from playground_dev import views

urlpatterns = [
    path("methods/", views.Methods.as_view({"get": "methods_list"})),
    path("methods/<str:method>/", views.Methods.as_view({"get": "method_retrieve"}))
]
