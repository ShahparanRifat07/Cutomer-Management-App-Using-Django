from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def homeView(request):
    customers = Customers.objects.all()
    order = Order.objects.all()
    total_customers =customers.count()
    total_orders = order.count()
    delivered=order.filter(status='Delivered').count()
    pending = order.filter(status='Pending').count()
    
    context = {
        'orders': order,
        'customers': customers,
        'total_orders':total_orders,
        'delivered':delivered,
        'pending':pending,
        
    }
    return render(request,'accounts/index.html',context)

def productView(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{'products':products})

def customerView(request,pk):
    customer = Customers.objects.get(pk=pk)
    orders= customer.order_set.all()
    total_order=orders.count()
    context={
        'customer':customer,
        'orders':orders,
        'total_order':total_order,
    }
    return render(request,'accounts/customers.html',context)

def createOrder(request):
    form = OrderForm()
    if(request.method == 'POST'):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        context={
            'form':form,
        }
        return render(request,'accounts/order_form.html',context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if(request.method == 'POST'):
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={
        'form':form,
    }
    return render(request,'accounts/order_form.html',context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if(request.method == 'POST'):
        order.delete()
        return redirect('/')    
    context={
        'order':order,
    }
    return render(request,'accounts/delete_order.html',context)