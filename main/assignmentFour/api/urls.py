from assignmentFour.api.views import EmployeeDetail, EmployeeList
from django.urls import path

urlpatterns = [
    path("list1/", EmployeeList.as_view(), name="EmployeeList"),
    path("list/<int:pk>", EmployeeDetail.as_view(), name="EmployeeDetail"),
]
