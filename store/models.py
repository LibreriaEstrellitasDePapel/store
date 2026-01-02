from django.conf import settings
from django.db import models
User = settings.AUTH_USER_MODEL
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,related_name='books')
    def __str__(self):
        return self.title
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)