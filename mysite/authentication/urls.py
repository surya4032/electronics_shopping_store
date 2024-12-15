from django.urls import path
from .views import UserRegisterView, Login, CustomPasswordResetCompleteView, CustomPasswordResetConfirmView, CustomPasswordResetDoneView, CustomPasswordResetView
from .views import profile_view

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/',UserRegisterView.as_view(), name='reg'),
    path('login/', Login.as_view(),name='login'),
    
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', profile_view, name='profile'),
]
