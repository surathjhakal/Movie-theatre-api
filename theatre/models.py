from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=16, null=False, unique=True)
    ticket_id = models.IntegerField(null=False, unique=True)
    seat_no = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}  -  ticket id: {self.ticket_id}"
