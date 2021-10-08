from django.urls import path, include
from django.conf.urls import handler404 #for 404 error not working
#here we have imported all the class views.
from .views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,PostDeleteView
urlpatterns = [
    # path('', views.home, name='ecommerce-home'),  --> for function based view
    #for home page
    path('', ProductListView.as_view(), name='ecommerce-home'),

    #for product update passing integer primary key to reach a specific product
    path('product/<int:pk>/update/',ProductUpdateView.as_view(), name="ecommerce-update-product"),

    # for product delete passing integer primary key to delete a specific product
    path('product/<int:pk>/delete/', PostDeleteView.as_view(), name="ecommerce-delete-product"),

    #for creating  a new product using  new endpoint
    path('product/new/',ProductCreateView.as_view(), name="ecommerce-add-product"),

    # for product detial view passing integer primary key to reach a specific product
    path('product/<int:pk>/', ProductDetailView.as_view(), name="ecommerce-product"),


]

