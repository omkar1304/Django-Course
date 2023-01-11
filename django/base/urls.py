"""practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    # query set
    path('queryset/', views.querySet, name='queryset'),

    # pagination
    path('paginationf/', views.pagination, name='paginationf'),
    path("paginationc/", views.PaginatorView.as_view(), name="paginationc"),

    # function based view V/S class based view
    path('studentlistf/', views.studentList, name='studentlist-f'),
    path('studentlistc/', views.StudentList.as_view(), name='studentlist-c'),

    path('studentdetailf/<str:pk>/', views.studentDetail, name='studentdetail-f'),
    path('studentdetailc/<str:pk>/', views.StudentDetail.as_view(), name='studentdetail-c'),

    path('studentcreatef/', views.studentCreate, name='studentcreate-f'),
    path('studentcreatec/', views.StudentCreate.as_view(), name='studentcreate-c'),

    path('studentupdatef/<str:pk>/', views.studentUpdate, name='studentupdate-f'),
    path('studentupdatec/<str:pk>/', views.StudentUpdate.as_view(), name='studentupdate-c'),

    path('studentdeletef/<str:pk>/', views.studentDelete, name='studentdelete-f'),
    path('studentdeletec/<str:pk>/', views.StudentDelete.as_view(), name='studentdelete-c'),

    # user functionality
    path('usersignupform/', views.user_signup_form, name='usersignupform'),
    path('usersignupform2/', views.user_signup_form2, name='usersignupform2'),
    path('userlogin/', views.user_login, name='userlogin'),
    path('userlogout/', views.user_logout, name='userlogout'),
    path('userupdateform/', views.user_update_form, name='userupdateform'),
    path('userupdateform2/', views.user_update_form2, name='userupdateform2'),
    path('userpasswordupdatewithold/', views.user_password_update_with_old, name='userpasswordupdatewithold'),
    path('userpasswordupdatewithoutold/', views.user_password_update_without_old, name='userpasswordupdatewithoutold'),


]
