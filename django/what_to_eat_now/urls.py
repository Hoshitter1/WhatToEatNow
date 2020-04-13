"""what_to_eat_now URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib import admin
from rest_framework import routers

from user_detail.views import UserDetailUpdateView
from options.views import FoodOptionsView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'userdetail', UserDetailUpdateView)

urlpatterns = [
    path('api/options', FoodOptionsView.as_view()),  # To get what kind of food options there is
    path('api/', include(router.urls)),  # DRF
    path('admin/', admin.site.urls),
    path('auth/', include('allauth.urls')),  # social login
    path('linebot/', include('line_bot_app.urls')),  # Linebot
    path('', include('link.urls')),  # linking social account
]
