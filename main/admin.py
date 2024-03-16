from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Announcements, Articles, OwnersOfGreatHearts, MainNews, YoungReception, Privileges, Report, Partners

admin.site.unregister((Group))

admin.site.register((Announcements, Articles, OwnersOfGreatHearts, MainNews, YoungReception, Privileges, Report,
                     Partners))
