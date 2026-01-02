from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from .models import Cart,CartItem
@receiver(post_save, sender=User)
def create_cart(sender,instance,created,**kwargs):
    if created:
        Cart.objects.create(user=instance)
@receiver(user_logged_in)
def merge_cart(sender, request, user, **kwargs):
    session_cart = request.session.get('cart')
    if not session_cart:
        return
    cart = user.cart
    for book_id, qty in session_cart.items():
        item, created = CartItem.objects.get_or_create(cart=cart,book_id=book_id)
        if not created:
            item.quantity += qty
        else:
            item.quantity = qty
        item.save()
    del request.session['cart']