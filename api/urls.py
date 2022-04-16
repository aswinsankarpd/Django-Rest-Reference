from django.urls import path
from .views import index,drink_detail

urlpatterns = [
    path('drinks/', index),
    path('drink_detail/<int:id>',drink_detail),
]