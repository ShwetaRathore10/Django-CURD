from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.CharField(max_length=12, default=90)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.username}, {self.password}"
    
class Restaurants(models.Model):
    Res_name = models.CharField(max_length=100)
    Food_cat = models.CharField(max_length=200)
    rating = models.FloatField()
    img = models.URLField(default="")
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.Res_name   

class Menu(models.Model):
    res = models.ForeignKey(
        Restaurants,
        on_delete=models.CASCADE
    )  
    item_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.item_name} - {self.res.Res_name}" 