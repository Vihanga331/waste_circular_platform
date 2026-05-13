from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("forgot-password/", views.forgot_password_view, name="forgot_password"),
    path("verify-email/", views.verify_email_view, name="verify_email"),
    path("profile/", views.profile_view, name="profile"),
    path("sessions/", views.sessions_view, name="sessions"),
]
