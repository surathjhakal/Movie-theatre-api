from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "ticket_id", "seat_no")


admin.site.register(User, UserAdmin)
