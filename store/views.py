from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CartItem,Book,Category
def catalog(request):
    category_id=request.GET.get('category')
    categories=Category.objects.all()
    if category_id:
        books=Book.objects.filter(category_id=category_id)
    else:
        books=Book.objects.all()
    return render(request,'store/catalog.html',{'books': books,'categories': categories,})
@login_required
def add_to_cart(request, book_id):
    if request.user.is_authenticated:
        cart = request.user.cart
        item, created = CartItem.objects.get_or_create(cart=cart,book_id=book_id)
        if not created:
            item.quantity+=1
            item.save()
    else:
        cart = request.session.get('cart', {})
        cart[str(book_id)] = cart.get(str(book_id), 0)+1
        request.session['cart'] = cart
    return redirect('catalog')
@login_required
def view_cart(request):
    if request.user.is_authenticated:
        items = request.user.cart.items.all()
        return render(request, 'store/cart.html', {'items': items})
    cart = request.session.get('cart', {})
    books = []
    for book_id, qty in cart.items():
        book = Book.objects.get(id=book_id)
        book.quantity = qty
        books.append(book)
    return render(request, 'store/cart.html', {'session_books': books})
@login_required
def remove_from_cart(request, book_id):
    cart = request.user.cart
    CartItem.objects.filter(cart=cart,book_id=book_id).delete()
    return redirect('view_cart')
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, 'store/register.html', {'form': form})