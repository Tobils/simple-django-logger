from django.urls import path, include
from .views import test_logger

urlpatterns = [
  path("logger/", test_logger, name="logger")
]
