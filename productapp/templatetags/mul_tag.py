from django import template
from cart.cart import Cart
register = template.Library()

@register.simple_tag
def multiply(qty, unit_price, *args, **kwargs):
    # you would need to do any localization of the result here
    return int(qty) * int(unit_price)

@register.simple_tag
def check(qty):
    qty = int(qty)
    if qty==1:
        return ""
    else:
        return 'class="disabled"'
    
@register.filter(name='total_cart_price')  
def total_amount_cart(products,request):
    cart = Cart(request)
    #print(products)
    # for item in cartitems():
    #         print(item['price'])
    sumv = sum(int(d['price'])*int(d['quantity']) for d in products.values() if d) 
    #print(sumv)
    return sumv
    
    
    