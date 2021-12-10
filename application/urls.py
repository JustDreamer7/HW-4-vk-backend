"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tenders.views import TenderViewSet, index, TenderView
from users.views import UserViewSet, login, home

router = DefaultRouter()
router.register(r'api/tenders', TenderViewSet, basename='tenders')
router.register(r'api/users', UserViewSet, basename='users')
# router.register(r'api/tendersearch', TenderView, basename='tendersearch')
# router.register(r'api/test', AddTenderViewSet, basename='test')
urlpatterns = [
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('tenders/', include('tenders.urls')),
    path('users/', include('users.urls')),
    path('social_auth/', include('social_django.urls', namespace='social')),
    path('homepage/', index, name='index')
]

urlpatterns += router.urls
