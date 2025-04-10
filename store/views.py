from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('book_list')
        else:
            return render(request, 'store/register.html', {'error': 'Username already exists'})
    return render(request, 'store/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'store/book_list.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'store/book_detail.html', {'book': book})

@login_required
def view_cart(request):
    # Initialize cart as dictionary if it doesn't exist
    if 'cart' not in request.session or not isinstance(request.session['cart'], dict):
        request.session['cart'] = {}
    
    cart = request.session['cart']
    
    # Convert string keys to integers for query
    book_ids = [int(id) for id in cart.keys() if id.isdigit()]
    books = Book.objects.filter(id__in=book_ids)
    
    cart_items = []
    subtotal = 0
    
    for book in books:
        # Use string key to access quantity
        quantity = cart.get(str(book.id), 0)
        if quantity > 0:
            item_total = book.price * quantity
            subtotal += item_total
            cart_items.append({
                'book': book,
                'quantity': quantity,
                'item_total': item_total
            })
    
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal
    })

@login_required
def add_to_cart(request, book_id):
    # Initialize cart as dictionary if needed
    if 'cart' not in request.session or not isinstance(request.session['cart'], dict):
        request.session['cart'] = {}
    
    cart = request.session['cart']
    book_id_str = str(book_id)
    
    # Update quantity
    cart[book_id_str] = cart.get(book_id_str, 0) + 1
    
    # Mark session as modified
    request.session.modified = True
    return redirect('view_cart')
