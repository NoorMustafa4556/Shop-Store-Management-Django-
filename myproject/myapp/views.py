# views.py (UPDATED FOR STORE)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Customer, Order

# ==============================================================================
#  HELPER FUNCTION: Isse hum har jagah istemal karenge
# ==============================================================================
def get_or_create_customer_profile(user):
    
    customer, created = Customer.objects.get_or_create(
        user=user,
        defaults={
            'name': user.get_full_name() or user.username,
            'email': user.email
        }
    )
    return customer

# ==============================================================================
#  MAIN VIEWS
# ==============================================================================

def home(request):
    search_query = request.GET.get('search', '')
    products = Product.objects.all()
    categories = Category.objects.all()
    
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(category__name__icontains=search_query)
        ).distinct()

    context = {
        'products': products,
        'categories': categories,
        'search_query': search_query,
    }
    return render(request, 'home.html', context)

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all() 
    context = {
        'products': products, 'category': category, 'categories': categories,
    }
    return render(request, 'category_products.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    already_requested = False
    
    if request.user.is_authenticated:
        customer = get_or_create_customer_profile(request.user)
        # Check karein ke 'Pending' ya 'Approved' status wali request hai ya nahi
        already_requested = Order.objects.filter(
            customer=customer, 
            product=product, 
            status__in=['Pending', 'Approved'] # In dono status ko check karein
        ).exists()
            
    context = {
        'product': product,
        'already_requested': already_requested,
    }
    return render(request, 'product_detail.html', context)

def request_product(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request, "Please log in to request products.")
        return redirect('login')

    if request.method == 'POST': # Best practice is to check for POST method
        product = get_object_or_404(Product, id=pk)
        customer = get_or_create_customer_profile(request.user)

        # Safety Check: Dobara check karein ke request pehle se to nahi hai
        if Order.objects.filter(customer=customer, product=product, status__in=['Pending', 'Approved']).exists():
            messages.warning(request, "You have already sent a request for this product.")
            return redirect('product_detail', pk=product.id)
        
        Order.objects.create(customer=customer, product=product, status='Pending')
        messages.success(request, f"Your request for '{product.name}' has been submitted!")
        return redirect('my_requests')

    # Agar GET request aaye to detail page par wapas bhej dein
    return redirect('product_detail', pk=pk)

def my_requests(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    customer = get_or_create_customer_profile(request.user)
    requests = Order.objects.filter(customer=customer).order_by('-date_requested')
    context = {'requests': requests}
    return render(request, 'my_requests.html', context)

# ==============================================================================
#  AUTHENTICATION VIEWS
# ==============================================================================

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        user = User.objects.create_user(
            username=username, email=email, password=password,
            first_name=first_name, last_name=last_name
        )
        Customer.objects.create(
            user=user, name=f"{user.first_name} {user.last_name}", email=user.email
        )
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username_or_email, password=password)
        if user is None:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
                
        if user is not None:
            login(request, user)
            get_or_create_customer_profile(user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username/email or password.")
            return redirect('login')
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')