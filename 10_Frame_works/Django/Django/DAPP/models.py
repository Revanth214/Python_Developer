from django.db import models

# Create your models here.

# class Country(models.Model):
#     Name=models.CharField()
#     Prime_minister=models.CharField()
#     No_of_states=models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name
