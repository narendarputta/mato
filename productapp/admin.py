from django.contrib import admin
from .models import Products,Customer,Order

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('name', 'price', 'image', 'description')
    # add filtering by date
    list_filter = ('name',)
    # add search field 
    search_fields = ['name', 'price']

admin.site.register(Products, CommentAdmin)


class CustomerAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('first_name', 'last_name', 'username', 'email','phone','password')
    # add filtering by date
    list_filter = ('username','email','phone')
    # add search field 
    search_fields = ['username', 'email','phone']

admin.site.register(Customer, CustomerAdmin)


class OrderAdmin(admin.ModelAdmin):
    # define which columns displayed in changelist
    list_display = ('product_id', 'user_id', 'address', 'phonenumber','price','total')
    # add filtering by date
    list_filter = ('address','user_id','product_id')
    # add search field 
    search_fields = ['address', 'user_id','product_id']
    


admin.site.register(Order,OrderAdmin)




