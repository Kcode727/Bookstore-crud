from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from .models import Book
from decimal import Decimal

class register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('book_list')

class user_login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('book_list')
        messages.error(request, 'Invalid credentials')
        return redirect('login')

class user_logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class AdminPanelView(View):
    def get(self, request):
        if not request.user.is_staff:
            messages.error(request, 'Access denied')
            return redirect('login')
        books = Book.objects.all()
        return render(request, 'admin_panel.html', {'books': books})

class AdminBookFormView(View):
    def get(self, request, pk=None):
        book = Book.objects.get(pk=pk) if pk else None
        return render(request, 'admin_book_form.html', {'book': book})

    def post(self, request, pk=None):
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        if not all([title, author, price, stock]):
            messages.error(request, 'All fields are required')
            return redirect('admin_book_form')
        if pk:
            book = Book.objects.get(pk=pk)
            book.title = title
            book.author = author
            book.price = price
            book.stock = stock
            book.save()
        else:
            Book.objects.create(title=title, author=author, price=price, stock=stock)
        return redirect('admin_panel')

# Function-based views
def admin_dashboard(request):
    books = Book.objects.all()
    return render(request, 'admin_dashboard.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        description = request.POST['description']
        Book.objects.create(
            title=title,
            author=author,
            price=price,
            description=description
        )
        return redirect('admin_dashboard')
    return render(request, 'add_book.html')

def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)
    return redirect('admin_dashboard')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

class book_detail(View):
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        return render(request, 'book_detail.html', {'book': book})

class add_to_cart(View):
    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        cart = request.session.get('cart', {})
        cart[str(pk)] = cart.get(str(pk), 0) + 1
        request.session['cart'] = cart
        messages.success(request, f'{book.title} added to cart')
        return redirect('book_list')

class view_cart(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        books = []
        total = Decimal('0.00')
        for book_id, quantity in cart.items():
            book = Book.objects.get(pk=book_id)
            subtotal = book.price * quantity
            books.append({'book': book, 'quantity': quantity, 'subtotal': subtotal})
            total += subtotal
        return render(request, 'cart.html', {'cart_items': books, 'total': total})
