from django.urls import path
from . import views

urlpatterns = [
    path('stock/',views.index),
    path('stock/<int:user_id>/analyze/',views.analyze)
]