# have to bring path package in and views
from django.urls import path

# url for home page
from . import views

urlpatterns = [
    # routing template
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]
