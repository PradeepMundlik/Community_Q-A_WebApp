from django.contrib import admin
from django.urls import path,include
from QandA import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login',views.Login, name='login'),
    path('logout',views.Logout, name='logout'),
    path('createNewAccount',views.create_new_accout, name='createNewAccount')

]