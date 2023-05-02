from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Student(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
