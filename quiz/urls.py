from django.urls import path

from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('dashboard/',dashboard,name='dashboard'),
    path('login/',login_html,name='login'),
    path('login-enter/',login_page,name='login-enter'),
    path('quiz_page/',quiz_page,name='quiz_page'),
    path('result',result,name='result'),
    path('settings/',settings,name='settings'),
    path('logout/',login_page,name="logout"),
]

