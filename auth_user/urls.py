from django.urls import path
from .views import *

urlpatterns=[
    path('login_/',login_,name='login_'),
    path('register/',register,name='register'),
    path('home/',home,name='home'),
    path('logout_/',logout_,name='logout_'),
    path('profile/',profile,name='profile'),
    path('update/',update,name='update'),
    path('reset/',reset,name='reset'),
    path('fpaswd/',fpaswd,name='fpaswd'),
    path('validp/',validp,name='validp'),
    path('upprofile/',upprofile,name='upprofile')
]