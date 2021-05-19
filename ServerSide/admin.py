from django.contrib import admin
from .models import Stations,Customers, Items, Payments

# Register your models here.
admin.site.register([Stations,Customers, Items, Payments])
