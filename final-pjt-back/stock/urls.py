from django.urls import path
from . import views

urlpatterns = [
    path('stock/analyze/',views.analyze),
    path('token/',views.get_token)
    # path('stock/analyze/',views.analyze),
]