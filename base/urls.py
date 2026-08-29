app_name = 'base'
from django.urls import path
from .views import *

urlpatterns=[
    path('home/',home,name='home'),
    path('add/',add,name='add'),
    path('delete/<int:pk>',delete,name='delete'),
    path('trash/',trash,name='trash'),
    path('pdelete/',pdelete,name='pdelete'),
]