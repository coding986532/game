from django.urls import path
from . import views
urlpatterns = [
    path('', views.Listings, name='index'),
    path('buy', views.buy, name='buy'),
    path('callback', views.callback, name='callback'),
    path('methodselect', views.methodselect, name='methodselect'),
    path('payment', views.payment, name='payment'),
]
