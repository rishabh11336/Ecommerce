from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.Sign_in, name='Sign_in'),

]