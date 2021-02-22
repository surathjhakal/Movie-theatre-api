from django.conf import settings
from .models import User
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
MAX_OCCUPANCY = settings.MAX_OCCUPANCY
d = User.objects.all()
UserLen = len(d) if d.exists() else 0


def index(request):
    return HttpResponse(f"Hello your are at the home page of theatre app    |||   There are {MAX_OCCUPANCY-UserLen} seats left!!")


def occupy(request, name, ticket_id):
    if User.objects.all().exists():
        userObjectsLen = len(User.objects.all())
        if MAX_OCCUPANCY > userObjectsLen:
            print(MAX_OCCUPANCY, userObjectsLen)
            sortedForm = User.objects.order_by('seat_no')
            f = sortedForm.values('seat_no')
            j = 1
            for i in f:
                if i['seat_no'] != j:
                    break
                j += 1
            user = User(name=name, ticket_id=ticket_id, seat_no=j)
            user.save()
            return HttpResponse(f"Hello {name}, your seat no. is {j}")
        else:
            print(MAX_OCCUPANCY, userObjectsLen)
            return HttpResponse("There are no more seats left, sorry try again later!!")
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
        return HttpResponse("You can't vacate because there is no user")


def get_info(request, seat_info):
    if User.objects.all().exists():
        data = None
        checkString = True
        try:
            seat_info = int(seat_info)
            checkString = False
        except ValueError:
            pass
        if checkString:
            if User.objects.filter(name=seat_info).exists():
                data = User.objects.get(name=seat_info)
        else:
            data = User.objects.filter(ticket_id=seat_info).exists()
            if data:
                data = User.objects.get(ticket_id=seat_info)
            else:
                data = User.objects.filter(seat_no=seat_info).exists()
                if data:
                    data = User.objects.get(seat_no=seat_info)
        if data:
            return HttpResponse(f"Your ticket info is as follows : \n {data}")
        else:
            return HttpResponse("There no user present so correctly enter the details")
    else:
        return HttpResponse("You can't get the info because no user has been created")
