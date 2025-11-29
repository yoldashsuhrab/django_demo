from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='account_login'),
]

