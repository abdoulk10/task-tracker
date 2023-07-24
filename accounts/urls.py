from django.urls import path
from accounts.views import login_form, logout_form, signup_form

urlpatterns = [
    path("signup/", signup_form, name="signup"),
    path("logout/", logout_form, name="logout"),
    path("login/", login_form, name="login"),
]
