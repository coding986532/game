from django.urls import path
from . import views
urlpatterns = [
  #  path('', views.home, name='home'),
    path('job-offers', views.joblistings, name='job-offers'),
    path('apply/<int:jobid>', views.jobsapply, name="apply")
    
]
