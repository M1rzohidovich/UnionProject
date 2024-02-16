from django.contrib import admin
from .models import Directors, Employees, OTMLeaders, EOLeaders, PELeaders

admin.site.register((Directors, Employees, OTMLeaders, EOLeaders, PELeaders))


