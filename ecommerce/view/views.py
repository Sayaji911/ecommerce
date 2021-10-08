from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

#
def home(request): #rendunt code for showing all products.
    prods = {
        'products': Product.objects.all()
    }
    return render(request, 'view/home.html', prods)

#using class based view for showing all products which inherits from djago listview
class ProductListView(ListView):
    model = Product
    template_name = 'view/home.html'
    context_object_name = 'products'

#for showing detail of product inherits from detiaview
# defining the model we have created ant the templte name that we will render
class ProductDetailView(DetailView):
    model = Product
    template_name = 'view/product.html'

#class based view for creating new products
#inheriting from CreateView and passing SuccessMessageMixin for success message
#also passing the fields we want the to input into the fields
#showing success_messge.
class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    fields = ['name', 'brand', 'description', 'price', 'rating', 'image']
    template_name = 'view/addproduct.html'
    success_message = 'Product Added Successfully'

#same as create product
class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['name', 'brand', 'description', 'price', 'rating', 'image']
    template_name = 'view/addproduct.html'
    success_message = 'Product updated Successfully'

#creting product delete importing from DeleteView
class PostDeleteView(DeleteView):
    model = Product
    template_name = 'view/delete.html'
    success_url = '/'


