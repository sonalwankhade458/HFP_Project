from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField()

    def __str__(self):
        return self.name
