from turtle import home
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sender/', views.sender),
    path('receiver/', views.receiver),
    path('chatbot/', views.chatbot),
    path('external/', views.external),
    path('externalTwo/', views.externalTwo),
    path('ocr/', views.ocr),
]
