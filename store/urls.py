from django.urls import path
from .views import catalog, add_to_cart, view_cart

urlpatterns = [
    path('', catalog, name='catalog'),
    path('add/<int:book_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
]
