from django.db import models


class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    hireDate = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
