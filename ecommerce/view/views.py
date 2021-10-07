from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


def home(request):
    prods = {
        'products': Product.objects.all()
    }
    return render(request, 'view/home.html', prods)


class ProductListView(ListView):
    model = Product
    template_name = 'view/home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'view/product.html'


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    fields = ['name', 'brand', 'description', 'price', 'rating', 'image']
    template_name = 'view/addproduct.html'
    success_message = 'Product Added Successfully'


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['name', 'brand', 'description', 'price', 'rating', 'image']
    template_name = 'view/addproduct.html'
    success_message = 'Product Added Successfully'

class PostDeleteView(DeleteView):
    model = Product
    template_name = 'view/delete.html'
    success_url = '/'


