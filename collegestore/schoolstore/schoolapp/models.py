from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=80)
    dept = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Course(models.Model):
    dept = models.CharField(max_length=80)
    course = models.CharField(max_length=100)

    def __str__(self):
        return str(self.course)
