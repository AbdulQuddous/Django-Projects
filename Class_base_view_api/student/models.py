from django.db import models

# Create your models here.
class Student_data(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    cgpa = models.FloatField()
    email = models.EmailField(unique=True,max_length=254)

    def __str__(self):
        return self.name
