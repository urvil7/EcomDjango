from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    Name = models.CharField(max_length=50)
    Description = models.TextField(max_length=100)
    Image = models.ImageField(default='default.jpg',upload_to='images')

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=50)
    CategoryId = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    Quntity = models.IntegerField()
    Size = models.CharField(max_length=10)
    Color = models.CharField(max_length=20)
    Image = models.ImageField(default = 'default.jpg',upload_to='images')

    def __str__(self):
        return self.Name

class Order(models.Model):
    Name = models.CharField(max_length=50)
    ProductId = models.ForeignKey(Product,on_delete=models.CASCADE)
    UserId = models.ForeignKey(User,on_delete=models.CASCADE)
    Size = models.CharField(max_length=10)
    Color = models.CharField(max_length=20)
    Quntity = models.IntegerField()
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    GrandTotal = models.DecimalField(max_digits=10,decimal_places=2)
    Image = models.ImageField(default = 'default.jpg',upload_to='images')

    def __str__(self):
        return self.Name