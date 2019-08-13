# have to bring path package in and views
from django.urls import path

# url for home page
from . import views

urlpatterns = [
    path('', views.index, name='index')  # this is the page
]
