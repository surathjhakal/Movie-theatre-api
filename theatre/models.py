from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=16, null=False, unique=True)
    ticket_id = models.IntegerField(null=False, unique=True)
    seat_no = models.IntegerField(default=0)

    def __str__(self):
        return f"||    Name : {self.name}    ||    Ticket ID : {self.ticket_id}    ||    Seat No : {self.seat_no}   || 😃😃😃"
