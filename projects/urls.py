from django.urls import path
from projects.views import list_projects
from tasks.views import show_project

urlpatterns = [
    path("<int:id>/", show_project, name="show_project"),
    path("", list_projects, name="list_projects"),
]
