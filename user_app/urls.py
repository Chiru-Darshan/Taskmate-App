from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', authViews.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout', authViews.LogoutView.as_view(template_name='logout.html'), name="logout"),
]