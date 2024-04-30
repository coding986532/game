from django.urls import path
from . import views
urlpatterns = [
  #  path('', views.home, name='home'),
    path('listings', views.listonsale, name='listings'),
    path('buy', views.buy, name='buy'),
    path('callback/<int:txid>', views.callback, name='callback'),
    path('methodselect/<int:txid>', views.methodselect, name='methodselect'),
    path('payment/<int:txid>', views.payment, name='payment'),
    path('details/<int:pk>', views.details, name='propdetails'),
    path('ingamepay', views.ingamepay, name='ingamepayemnt'),
]
