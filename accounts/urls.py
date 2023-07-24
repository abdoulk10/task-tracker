from django.urls import path
from accounts.views import login_form

urlpatterns = [
    path("login/", login_form, name="login"),
]
