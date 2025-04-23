from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register.as_view(), name='register'),
    path('login/', views.user_login.as_view(), name='login'),
    path('logout/', views.user_logout.as_view(), name='logout'),  
    path('book/<int:pk>/', views.book_detail.as_view(), name='book_detail'),
    path('add_to_cart/<int:pk>/', views.add_to_cart.as_view(), name='add_to_cart'),
    path('cart/', views.view_cart.as_view(), name='view_cart'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('books/', views.book_list, name='book_list'),
    path('admin_panel/', views.AdminPanelView.as_view(), name='admin_panel'),
    path('admin_book_form/', views.AdminBookFormView.as_view(), name='admin_book_form'),
    path('admin_book_form/<int:pk>/', views.AdminBookFormView.as_view(), name='edit_book'),
]
