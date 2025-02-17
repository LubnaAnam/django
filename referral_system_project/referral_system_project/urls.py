"""
URL configuration for referral_system_project project.

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
# path('api/register/', views.register_user),
    # path('api/user/', views.user_details),
    # path('api/referrals/', views.referrals),




from django.contrib import admin
from django.urls import path
from django.urls import path, include
from referral_system import views
from referral_system.views import register_user
from referral_system.views import user_details
from referral_system.views import referrals_list
from referral_system.views import ListUsers , CustomAuthToken


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', register_user, name='register_user'),
    path('api/user-details/', user_details, name='user_details'),
    path('api/referrals/', referrals_list, name='referrals_list'),
    path('api/token/auth/', CustomAuthToken.as_view()),

]




