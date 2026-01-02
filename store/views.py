from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Book,Category
def catalog(request):
    category_id=request.GET.get('category')
    categories=Category.objects.all()
    if category_id:
        books=Book.objects.filter(category_id=category_id)
    else:
        books=Book.objects.all()
    return render(request,'store/catalog.html',{'books': books,'categories': categories,})
def add_to_cart(request,book_id):
    cart=request.session.get('cart',{})
    cart[str(book_id)]=cart.get(str(book_id),0)+1
    request.session['cart']=cart
    return redirect('catalog')
def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0
    for book_id, quantity in cart.items():
        book = Book.objects.get(id=book_id)
        subtotal = book.price * quantity
        total += subtotal
        items.append({'book': book,'quantity': quantity,'subtotal': subtotal,})
    return render(request, 'store/cart.html', {'items': items,'total': total,})
def remove_from_cart(request,book_id):
    cart=request.session.get('cart',{})
    book_id=str(book_id)
    if book_id in cart:
        del cart[book_id]
    request.session['cart']=cart
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