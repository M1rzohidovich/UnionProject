from django.urls import path
from management.views import GetDirector, GetEmployees, GetEOLeaders, GetPELeaders, GetOTMLeaders

urlpatterns = [
    path('get-director', GetDirector.as_view(), name='get-director'),
    path('get-employees', GetEmployees.as_view(), name='get-employees'),
    path('get-otm', GetOTMLeaders.as_view(), name='get-otm'),
    path('get-education', GetEOLeaders.as_view(), name='get-education'),
    path('get-enterprise', GetPELeaders.as_view(), name='get-enterprise')

]