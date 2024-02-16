from django.urls import path
from main.views import GetAnnouncement, GetMainNews, GetOwners, GetArticle, GetReception, GetPrivileges

urlpatterns = [
    path('get-announcements', GetAnnouncement.as_view(), name='get-announcements'),
    path('get-article', GetArticle.as_view(), name='get-article'),
    path('get-news', GetMainNews.as_view(), name='get-news'),
    path('get-owners', GetOwners.as_view(), name='get-owners'),
    path('get-reception', GetReception.as_view(), name='get-reception'),
    path('get-privileges', GetPrivileges.as_view(), name='get-privileges')

]