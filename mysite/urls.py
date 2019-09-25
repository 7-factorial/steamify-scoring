"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.shortcuts import redirect


def redir_home(request):
    return redirect("steamify:steamifyhome")


urlpatterns = [
    path('', redir_home),
    path('steamify/', include('steamify.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # raise NotImplementedError("Todo : https://docs.djangoproject.com/en/2.2/topics/auth/default/#module-django.contrib.auth.views")
    # path('login/', auth_views.login, name='login'),
    # path('logout/', auth_views.logout, name='logout'),
]
