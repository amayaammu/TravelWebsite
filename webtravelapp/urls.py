from django.urls import path
from . import views
urlpatterns=[
    path('index2',views.index2,name='index2'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('register',views.register,name='register'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('getweb',views.getweb,name='getweb'),
    path('regi',views.regi,name='regi'),
    path('userin',views.userin,name='userin'),
    path('logout',views.logout,name='logout'),
    path('registerations',views.registerations,name='registeration')
    
    
]