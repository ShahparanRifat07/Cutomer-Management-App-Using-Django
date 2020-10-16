from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request,'accounts/index.html',{'name':"Rifat"})

def productView(request):
    return render(request,'accounts/products.html',{})

def customerView(request):
    return render(request,'accounts/customers.html',{})