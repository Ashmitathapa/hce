from django.shortcuts import render

# Create your views here.
from products.models import Product
from.models import Category
from rest_framework import generics

from rest_framework.filters import SearchFilter
from .serializers import CategorySerializer



def category_list(request):
    categories =Category.objects.all()
    return render (request,'categories/category_list.html',{'categories':categories})

def category_product(request):
    categories=Category.objects.all()
    products=Product.objects.all()
    return render (request,'categories/category_product.html',{'categories':categories, 'products':products})


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class =CategorySerializer
    filter_backends=[SearchFilter]
    search_fields=['name','description']

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class =CategorySerializer
    