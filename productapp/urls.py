from django.urls import path
from django.conf.urls import url


from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('about', views.about,name="about"),
    path('contact', views.contact,name="contactus"),
    path('profile', views.profile,name="profile"),
    path('products', views.products,name="products"),
    path('viewdetails/<id>', views.viewdetails,name="viewdetails"),
    path('accounts/login', views.login,name="login"),
    path('accounts/register', views.register,name="register"),
    path('accountregister/<str:error>/', views.accountregister,name="accountregister"),
    path('logout', views.logout,name="logout"),
    path('cart/checkout', views.checkout,name="checkout"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/cartinsert',views.cartinsert,name='cartinsert'),
    path('cart/cartpayment',views.cartPayment,name='cartPayment'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),
]