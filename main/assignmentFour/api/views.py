from assignmentFour.api.serializers import EmployeeSerializer
from assignmentFour.models import Employee
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class EmployeeList(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serial = EmployeeSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDetail(APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            serial = EmployeeSerializer(employee)
            return Response(serial.data, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"detail": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)  # noqa: E501

    def put(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        serial = EmployeeSerializer(employee, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        else:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
