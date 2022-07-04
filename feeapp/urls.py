
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('courses/',views.courses,name='courses'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact/',views.contact,name='contact'),


    path('studenthome/',views.studenthome,name='studenthome'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('adminhome/',views.adminhome,name='adminhome'),
    path('staffhome/',views.staffhome,name='staffhome'),
    path('studentprofile/<str:pk_test>',views.studentprofile,name='studentprofile'),
    path('profileupdate/<str:pk_test>',views.profileupdate,name='profileupdate'),



    
    path('addcourse/',views.addcourse,name='addcourse'),
    path('delcourse/<str:pk_test>/',views.delcourse,name='delcourse'),
    path('delstudent/<str:pk_test>/',views.delstudent,name='delstudent'),

    

    

]
