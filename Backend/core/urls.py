from django.urls import path
from django.urls import path
from .views import trend_list,create_region

urlpatterns = [
    path('trends/', trend_list),
    path("trends/create/", create_region),
]
