from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('listings', views.Listings, name='listings'),
    path('buy', views.buy, name='buy'),
    path('callback', views.callback, name='callback'),
    path('methodselect', views.methodselect, name='methodselect'),
    path('payment', views.payment, name='payment'),
]
