from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_email = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Contact(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Subject = models.CharField(max_length=50)
    Message = models.TextField(max_length=100)

    def __str__(self):
        return self.Name