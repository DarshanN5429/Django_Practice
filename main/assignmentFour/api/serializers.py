from assignmentFour.models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firstName = serializers.CharField()
    lastName = serializers.CharField()
    email = serializers.EmailField()
    phoneNumber = serializers.CharField()
    hireDate = serializers.DateField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get("firstName", instance.firstName)  # noqa: E501
        instance.lastName = validated_data.get("lastName", instance.lastName)  # noqa: E501
        instance.email = validated_data.get("email", instance.email)
        instance.phoneNumber = validated_data.get("phoneNumber", instance.phoneNumber)  # noqa: E501
        instance.hireDate = validated_data.get("hireDate", instance.hireDate)
        instance.active = validated_data.get("active", instance.active)
        instance.save()
        return instance
