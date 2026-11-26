from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_datetime.urls')),
    path('', include('app_weather.urls')),
    path('', include('app_store.urls')),
]

