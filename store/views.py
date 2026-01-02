from django.shortcuts import redirect,render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import CartItem,Book,Category,Cart
def catalog(request):
    category_id=request.GET.get('category')
    categories=Category.objects.all()
    if category_id:
        books=Book.objects.filter(category_id=category_id)
    else:
        books=Book.objects.all()
    return render(request,'store/catalog.html',{'books':books,'categories':categories,})
@login_required
def add_to_cart(request,book_id):
    if request.user.is_authenticated:
        cart,_=Cart.objects.get_or_create(user=request.user)
        item,created=CartItem.objects.get_or_create(cart=cart,book_id=book_id)
        if not created:
            item.quantity+=1
            item.save()
    else:
        cart=request.session.get('cart',{})
        cart[str(book_id)]=cart.get(str(book_id),0)+1
        request.session['cart']=cart
    return redirect('catalog')
@login_required
def view_cart(request):
    cart,_=Cart.objects.get_or_create(user=request.user)
    items=cart.items.all()
    total=cart.total()
    return render(request,"store/cart.html",{"items":items,"total":total,})
@login_required
def remove_from_cart(request,book_id):
    cart,_=Cart.objects.get_or_create(user=request.user)
    CartItem.objects.filter(cart=cart,book_id=book_id).delete()
    return redirect('view_cart')
def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()
    return render(request,'store/register.html',{'form':form})
@login_required
def increase_quantity(request,item_id):
    item=get_object_or_404(CartItem,id=item_id,cart__user=request.user)
    item.quantity+=1
    item.save()
    return redirect("view_cart")
@login_required
def decrease_quantity(request,item_id):
    item=get_object_or_404(CartItem,id=item_id,cart__user=request.user)
    if item.quantity>1:
        item.quantity-=1
        item.save()
    else:
        item.delete()
    return redirect("view_cart")
def book_detail(request, book_id):
    book=get_object_or_404(Book,id=book_id)
    return render(request,"store/book_detail.html",{"book":book})