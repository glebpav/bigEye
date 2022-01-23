from django.db import models


class DataCollection(models.Model):
    rating = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    employeeId = models.CharField(max_length=255)

    def __str__(self):
        return self.rating

class Employee(models.Model):
    fio = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.fio
