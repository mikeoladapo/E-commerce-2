from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    phonenumber = models.CharField(max_length=12 )
    picture = models.ImageField(upload_to='profile_pics',blank=True,null=True)
    @property
    def username(self):
        return self.user.username

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    about = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='product_pics',blank=True,null=True)
    @property
    def category_name(self):
        return self.category.name 

    def __str__(self):
        return self.name
