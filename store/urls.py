from store.views import catalog,add_to_cart,remove_from_cart,view_cart,register,increase_quantity,decrease_quantity
from django.urls import path
urlpatterns=[
    path('',catalog,name='catalog'),
    path('add/<int:book_id>/',add_to_cart,name='add_to_cart'),
    path('remove/<int:book_id>/',remove_from_cart,name='remove_from_cart'),
    path('cart/',view_cart,name='view_cart'),
    path('register/',register,name='register'),
    path("cart/increase/<int:item_id>/",increase_quantity,name="increase_quantity"),
    path("cart/decrease/<int:item_id>/",decrease_quantity,name="decrease_quantity"),
]