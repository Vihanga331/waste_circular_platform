from django.shortcuts import render


def login_view(request):
    return render(request, "accounts/login.html", {"title": "Login"})


def signup_view(request):
    return render(request, "accounts/signup.html", {"title": "Create Account"})


def forgot_password_view(request):
    return render(request, "accounts/forgot_password.html", {"title": "Reset Password"})


def verify_email_view(request):
    return render(request, "accounts/verify_email.html", {"title": "Verify Email"})


def profile_view(request):
    return render(request, "accounts/profile.html", {"title": "Profile Settings"})


def sessions_view(request):
    return render(request, "accounts/sessions.html", {"title": "Session Management"})
