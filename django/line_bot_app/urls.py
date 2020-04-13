from django.urls import path
from . import views

urlpatterns = [
    path('callback', views.LineCallBack.as_view()),
]
