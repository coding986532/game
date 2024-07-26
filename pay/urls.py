"""
URL configuration for pay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from payments import views
from security.views import logon as logon
from security.views import signup1 as signup
from security.views import logout_user as logout
from security.views import apilogon
from jobs.views import joblistings
urlpatterns = [
    path("admin/", admin.site.urls),
    path("" , views.home, name='index', ),
    path("listings/" , views.listonsale, name='listings-page', ),
    path('listing/', include('payments.urls')),
    path('jobs/', include('jobs.urls')),
   # path("accounts/", include("security.urls")),
    path("university/", include("university.urls")),
    path("accounts/login/", logon),
    path("accounts/signup/", signup),
    path("accounts/logout/", logout),
    path("apilogon", apilogon)
]
