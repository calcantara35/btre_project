# have to bring path package in and views
from django.urls import path

# url for home page
from . import views

urlpatterns = [
    # routing template
    path('', views.index, name='index'),
    path('about', views.about, name='about')

]
