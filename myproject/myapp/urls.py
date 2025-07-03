from django.urls import path
from . import views

urlpatterns = [
    # User-Facing Store URLs
    path('category/<slug:category_slug>/', views.category_products, name='category_products'),
    path('', views.home, name='home'),
    path('request_product/<str:pk>/', views.request_product, name='request_product'),
    path('my_requests/', views.my_requests, name='my_requests'),
    path('product/<str:pk>/', views.product_detail, name='product_detail'),

    # Authentication URLs for Users
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]