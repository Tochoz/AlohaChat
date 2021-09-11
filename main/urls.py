from django.urls import path
from . import auth, views, messanger

urlpatterns = [
    path('auth', auth.auth, name='auth'),
    path('home', messanger.homepage, name='home'),
    path('', views.introduce, name='mainpage'),
    path("send", messanger.send_message, name="send"),
]