from django.urls import path
from projects.views import list_projects, create_project
from tasks.views import show_project

urlpatterns = [
    path("create/", create_project, name="create_project"),
    path("<int:id>/", show_project, name="show_project"),
    path("", list_projects, name="list_projects"),
]
