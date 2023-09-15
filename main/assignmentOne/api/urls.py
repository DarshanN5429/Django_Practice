from assignmentOne.api.views import helloWorld
from django.urls import path

urlpatterns = [
    path("helloWorld/", helloWorld, name="helloWorld"),
]
