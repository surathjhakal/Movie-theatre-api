from django.urls import path
from . import views

urlpatterns = [
    # This url is used to get the index page
    path('', views.index, name="index"),

    path('occupy/<str:name>-<int:ticket_id>', views.occupy,
         name="occupy"),  # This url is used for occupying ticket

    # This url is used to vacate your booked seat
    path('vacate/<int:seat_no>', views.vacate, name="vacate"),

    # This url is used to get the information of ticket
    path('get_info/<seat_info>', views.get_info, name="get_info"),
]
