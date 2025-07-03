from django.contrib import admin
from .models import Customer, Product, Order, Tag, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    # Sirf wohi fields rakhein jo model mein hain
    list_display = ('name', 'email', 'user') 
    search_fields = ('name', 'email', 'user__username')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'customer', 'status', 'date_requested')
    list_filter = ('status', 'date_requested')
    search_fields = ('customer__name', 'product__name')
    list_editable = ('status',)
    actions = ['mark_approved', 'mark_rejected']

    def mark_approved(self, request, queryset):
        queryset.update(status='Approved')
    mark_approved.short_description = "Mark selected as Approved"

    def mark_rejected(self, request, queryset):
        queryset.update(status='Rejected')
    mark_rejected.short_description = "Mark selected as Rejected"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)