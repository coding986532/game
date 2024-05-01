from django.urls import path
from . import views
urlpatterns = [
  #  path('', views.home, name='home'),
    path('university-offers', views.uni_listing, name='uni-offers')
]
