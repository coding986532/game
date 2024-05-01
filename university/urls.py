from django.urls import path
from . import views
urlpatterns = [
  #  path('', views.home, name='home'),
    path('university-offer-details/<int:pk>', views.uni_listing_detail, name='uni-detail'),
    path('university-offers', views.uni_listing, name='uni-offers')
]
