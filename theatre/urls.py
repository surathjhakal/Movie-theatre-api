from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('occupy/<str:name>-<int:ticket_id>', views.occupy, name="occupy"),
]
