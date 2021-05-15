from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),

]