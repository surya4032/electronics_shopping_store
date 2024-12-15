from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #loader module helps load html templates
from . models import Product
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy

# Create your views here.
# def home(request):
#     return HttpResponse("This is home page")
def home(request):
    products=Product.objects.all()#products list stores all the objects (records in the database)
    context ={
        'prods':products,
    }
    #context is a dictionary
    template= loader.get_template("home.html")#to fetch the html template from taht path,
    return HttpResponse(template.render(context,request))

def about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render())
def prod(request):
    template = loader.get_template("addproduct.html")
    return HttpResponse(template.render())
def product_details(request,id):
    product =Product.objects.get(id=id)
    context ={
        'product':product
        # product is aautomatically converted to variable in this context
    }
    template = loader.get_template('prod_details.html')
    return HttpResponse(template.render(context,request))
class ProductList(ListView):
    # inheritance listview class from django
    model=Product
    template_name="products.html"
class AddProduct(CreateView):
    model= Product
    template_name="addProduct.html"  
    fields=[
        'name',
        'price',
        'description',
        'stock',
        'pic'
    ]
    #what ever the fiekd we want to renedr from m,odel we will add in fileds.
    success_url="/"
class EditProduct(UpdateView):
    model = Product
    template_name ="Editproduct.html"
    fields=[
        'name',
        'price',
        'description',
        'stock',
        'pic'
    ]
    success_url="/"

class DelProduct(DeleteView):
    model=Product
    template_name ='Delproduct.html'
    fields =[
        'name',
        'price',
        'description',
        'pic'
    ]
    success_url=reverse_lazy('products')
    

    # success_url='/'
def SearchView(request):
    query = request.GET.get('q1')
    results= Product.objects.filter(name__icontains=query)
    #results is a list of product object whre name ="query"
    context = {
        'prods' : results,
        'query' : query,
        'length': len(results) 
    }
    template = loader.get_template('search_results.html')
    return HttpResponse(template.render(context,request))





