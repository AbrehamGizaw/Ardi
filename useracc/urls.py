from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
app_name = 'useracc'

urlpatterns = [
    path('profile/<int:id>/', Profile.as_view(), name='profile'),
    path('profile/edit/', EditProfile.as_view(), name='edit_profile'),
    path('register/', Register.as_view(), name='register'),
    path('email-verify/<str:uidb64>/<str:token>/', EmailVerify.as_view(), name='email_verify'),
    path('activate/<int:user_id>/', Activate.as_view(), name='activate'),
    path('delete_user/<int:user_id>/', DeleteUser.as_view(), name='delete_user'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('staff-page/', StaffPage.as_view(), name='staff_page'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
]
