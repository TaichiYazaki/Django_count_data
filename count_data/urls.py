from . import views
from django.urls import path


urlpatterns = [
    path('', views.index),
    path('count', views.count),
    path('avg', views.avg)
]
