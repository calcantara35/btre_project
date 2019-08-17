# have to bring path package in and views
from django.urls import path


from . import views

urlpatterns = [
    # routing template
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')

]
