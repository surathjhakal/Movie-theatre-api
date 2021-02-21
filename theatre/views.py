from django.conf import settings
from django.urls.base import reverse
from .models import User
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
MAX_OCCUPANCY = settings.MAX_OCCUPANCY

print(User.objects.all().exists())


def index(request):
    print(User.objects.all())
    return HttpResponse("Hello your are at the home page of theatre app")


def occupy(request, name, ticket_id):
    if User.objects.all().exists():
        userObjectsLen = len(User.objects.all())
        if MAX_OCCUPANCY >= userObjectsLen:
            sortedForm = User.objects.order_by('seat_no')
            f = sortedForm.values('seat_no')
            print(f)
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


def vacate(request, seat_no):
    if User.objects.all().exists():
        seatNo = User.objects.filter(seat_no=seat_no)
        if seatNo:
            seatNo.delete()
            return HttpResponse("You have vacate that seat, thank you")
        return HttpResponse("There was no user on that seat, first to to occupy a seat")
    else:
        return HttpResponse("You can't vacate because you are not a user")
