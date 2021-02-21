from django.conf import settings
from django.urls.base import reverse
from .models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
MAX_OCCUPANCY = settings.MAX_OCCUPANCY


def index(request):
    print(User.objects.all())
    return HttpResponse("Hello your are at the home page of theatre app")


def occupy(request, name, ticket_id):
    if User.objects.all().exists():
        userObjectsLen = len(User.objects.all())
        if MAX_OCCUPANCY >= userObjectsLen:
            f = User.objects.values('seat_no')
            j = 1
            for i in f:
                if i['seat_no'] != j:
                    break
                j += 1
            user = User(name=name, ticket_id=ticket_id, seat_no=j)
            user.save()
            return HttpResponse(f"Hello {name}, your seat no. is {j}")
        userObjectsLen = len(User.objects.all)
    else:
        user = User(name=name, ticket_id=ticket_id, seat_no=1)
        user.save()
        return HttpResponse(f"Hello {name}, your seat no. is 1")
