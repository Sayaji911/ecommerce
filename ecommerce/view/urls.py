from django.urls import path, include
from django.conf.urls import handler404

from .views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,PostDeleteView
urlpatterns = [
    # path('', views.home, name='ecommerce-home'),
    path('', ProductListView.as_view(), name='ecommerce-home'),
    path('product/<int:pk>/update/',ProductUpdateView.as_view(), name="ecommerce-update-product"),
    path('product/<int:pk>/delete/', PostDeleteView.as_view(), name="ecommerce-delete-product"),

    path('product/new/',ProductCreateView.as_view(), name="ecommerce-add-product"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name="ecommerce-product"),


]

