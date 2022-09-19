from re import template
from django.urls import path
from django.contrib.auth import views
from .views import SignUpView

urlpatterns = [
    path('login/', views.LoginView.as_view(
        template_name='usuarios/login.html'
    ), name="login"),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('signup/', SignUpView.as_view(), name='signup'),    
]