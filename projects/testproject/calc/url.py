from django.conf.urls import url

from . import views

urlpattrens = [
    url('',views.home, name='home')
]