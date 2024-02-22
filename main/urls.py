from django.urls import path
from main.views import GetAnnouncement, GetMainNews, GetOwners, GetArticle, GetReception, GetPrivileges

urlpatterns = [
    path('get-announcements', GetAnnouncement.as_view(), name='get-announcements'),
    path('get-announcements/<int:id>/', GetAnnouncement.as_view(), name='announcements-detail'),
    path('get-article', GetArticle.as_view(), name='get-article'),
    path('get-article/<int:id>/', GetArticle.as_view(), name='article-detail'),
    path('get-news', GetMainNews.as_view(), name='get-news'),
    path('get-news/<int:id>/', GetMainNews.as_view(), name='mydata-detail'),
    path('get-owners', GetOwners.as_view(), name='get-owners'),
    path('get-owners/<int:id>/', GetOwners.as_view(), name='owner-detail'),
    path('get-reception', GetReception.as_view(), name='get-reception'),
    path('get-reception/<int:id>/', GetReception.as_view(), name='reception-detail'),
    path('get-privileges', GetPrivileges.as_view(), name='get-privileges'),
    path('get-privileges/<int:id>/', GetPrivileges.as_view(), name='privileges-detail')

]