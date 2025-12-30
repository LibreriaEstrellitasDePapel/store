from django.shortcuts import render
from .models import Book

def catalog(request):
    books = Book.objects.all()
    return render(request, 'store/catalog.html', {'books': books})
