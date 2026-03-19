from django.db import models

# Create your models here.
class Products(models.Model):
    product_title = models.CharField(max_length=20)
    product_description= models.TextField()
    product_price = models.IntegerField()

    def __str__(self):
        return self.product_title
    
