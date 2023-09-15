from assignmentThree.api.views import modelList
from django.urls import path

urlpatterns = [
    path("list1/", modelList, name="modelList"),
]
