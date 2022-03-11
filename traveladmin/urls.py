from django.urls import path
from . import views
urlpatterns=[
    path('index',views.index,name='index'),
    path('add_destination/',views.add_destination,name='add_destination'),
    path('view_destination/',views.view_destination,name='view_destination'),
    path('getdata',views.getdata,name='getdata'),
    path('edit/<int:trid>/',views.edit,name='edit'),
    path('update/<int:uid>/',views.update,name='update'),
    path('delete/<int:did>/)',views.delete,name='delete'),
    path('',views.adminlogin,name='adminlogin'),
    path('adlogin',views.adlogin,name='adlogin')
]