from django.db import models


# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    price =models.PositiveIntegerField()
    description = models.TextField()
    stock = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    # It is impossible to add the field 'created_at' with 'auto_now_add=True' to product without providing a default. This is because the database needs something to populate existing rows.
    pic= models.ImageField(upload_to="products/",null=True)
    def __str__self(self):
        return self.name
    
