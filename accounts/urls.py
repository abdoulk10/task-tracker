from django.urls import path
from accounts.views import login_form, logout_form

urlpatterns = [
    path("logout/", logout_form, name="logout"),
    path("login/", login_form, name="login"),
]
