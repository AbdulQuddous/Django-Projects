from django.db import models

class Student_data(models.Model):
    name = models.CharField(max_length=20)
    semester = models.CharField(max_length=10)
    contact = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
