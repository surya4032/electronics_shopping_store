from django.urls import path
from .import views
app_name = 'Cart'
urlpatterns=[

    path('cart/',views.viewCart,name = 'view_cart'),
    path('add/<int:product_id>',views.addToCart , name = 'add_to_cart'),
    path('remove_from_cart/<int:cart_item_id>',views.remove_from_cart,name='remove'),
     path('cart/add/<int:cart_item_id>/', views.add_quantity, name='add_quantity'),
    path('cart/remove/<int:cart_item_id>/', views.remove_quantity, name='remove_quantity'),
]