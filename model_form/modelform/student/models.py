from django.db import models

# Create your models here.
class Student(models.Model):
    user_name = models.CharField(max_length=8, unique=True)
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email= models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name