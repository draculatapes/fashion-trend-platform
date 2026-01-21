from django.urls import path
from django.urls import path
from .views import trend_list

urlpatterns = [
    path('trends/', trend_list),
]
