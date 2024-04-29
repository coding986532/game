from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('listings', views.listonsale, name='listings'),
    path('buy', views.buy, name='buy'),
    path('callback', views.callback, name='callback'),
    path('methodselect', views.methodselect, name='methodselect'),
    path('payment', views.payment, name='payment'),
    path('details/<int:pk>', views.details, name='propdetails')
]
