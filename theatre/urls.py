from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('occupy/<str:name>-<int:ticket_id>', views.occupy, name="occupy"),
    path('vacate/<int:seat_no>', views.vacate, name="vacate"),
    path('get_info/<seat_info>', views.get_info, name="get_info")
]
