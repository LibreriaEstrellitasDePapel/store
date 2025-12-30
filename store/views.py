from django.shortcuts import redirect, get_object_or_404, render
from .models import Book
from .models import Book

def catalog(request):
    books = Book.objects.all()
    return render(request, 'store/catalog.html', {'books': books})
def add_to_cart(request, book_id):
    cart = request.session.get('cart', {})
    cart[str(book_id)] = cart.get(str(book_id), 0) + 1
    request.session['cart'] = cart
    return redirect('catalog')
def view_cart(request):
    cart = request.session.get('cart', {})
    books = []
    total = 0
    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        subtotal = book.price * quantity
        total += subtotal
        books.append({
            'book': book,
            'quantity': quantity,
            'subtotal': subtotal
        })
    return render(request, 'store/cart.html', {
        'books': books,
        'total': total
    })