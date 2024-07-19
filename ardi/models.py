from django.db import models
from datetime import datetime
from django.urls import reverse


class Product(models.Model):
    category = models.CharField(max_length=100, default='marble')
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    area = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to='testimonial_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)  # Optional phone number
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Automatic timestamp on creation

    def __str__(self):
        return self.name

# class User(AbstractUser):
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=150)

#     def __str__(self):
#         return self.email

class Home(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.title

class HomeImage(models.Model):
    home = models.ForeignKey(Home, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.image.name
