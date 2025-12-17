from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('dashboard/',dashboard,name='dashboard'),
    path('login/',login,name='login'),
    path('quiz_page/',quiz_page,name='quiz_page'),
    path('result',result,name='result'),
    path('settings/',settings,name='settings')
]

