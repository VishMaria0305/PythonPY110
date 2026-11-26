from django.urls import path
from .views import datetime_view, dynamic_datetime_view

urlpatterns = [
    path('datetime/', datetime_view),
    path('dynamic_datetime/', dynamic_datetime_view),
]
