from django.urls import path
from . import views

urlpatterns = [
    path('stock/analyze/',views.analyze),
    # path('stock/analyze/',views.analyze),
]