from django.urls import path
from .views import api_index

app_name = "api"

urlpatterns = [
    path("", api_index, name="index"),
    path("auth/", api_index, name="auth"),
    path("households/", api_index, name="households"),
    path("collections/", api_index, name="collections"),
    path("methane/", api_index, name="methane"),
    path("billing/", api_index, name="billing"),
    path("analytics/", api_index, name="analytics"),
]
