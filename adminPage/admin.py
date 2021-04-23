from django.contrib import admin

# Register your models here.

from .models import Employee, Date, Availability

admin.site.register(Availability)
admin.site.register(Employee)
admin.site.register(Date)
