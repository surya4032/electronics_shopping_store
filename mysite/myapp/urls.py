from django.urls import path
from .import views # This path function helps configure teh path requestd and the view utlized
 #imorting the views,py from the same directiry .Now all the designed views are available herre

urlpatterns= [
    path('',views.home,name="homepage"), #no path is requested run this home view in views module
    path('about',views.about ,name="aboutpage"),
    path('product',views.AddProduct.as_view(),name="productpage"),
    path('products',views.ProductList.as_view(),name="products"),
    path('prod_details/<int:id>' ,views.product_details , name ="p_details"),
    #int:id -path converter.
    path('editprod/<int:pk>',views.EditProduct.as_view(),name='edit_Prod'),
    path('Deleteprod/<int:pk>',views.DelProduct.as_view(),name ='delprod'),
    path('search/',views.SearchView,name='search')
]
