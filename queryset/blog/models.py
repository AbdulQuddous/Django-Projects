from django.db import models

class Student(models.Model):
    name= models.CharField(max_length=20,blank=True)
    marks =models.IntegerField()
    city=models.TextField()

    def __str__(self):
        return self.name
    
