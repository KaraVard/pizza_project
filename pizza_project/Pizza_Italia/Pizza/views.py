from django.shortcuts import render
from .models import Order, Pizza
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def home(request):
    """Returns home page"""
    p_obj = Pizza.objects.all()
    p_names = set(obj.name for obj in p_obj)
    p_sizes = set(obj.pizza_size for obj in p_obj)
    return render(request, 'Pizza/home.html', {'names': p_names, 'sizes': p_sizes})


def order(request):
    """
    Generates new order and returns order page
    """
    order_data = {
                 'c_name': request.GET['c_name'],
                 'pizza': request.GET['pizza'],
                 'pizza_size': request.GET['size'],
                 'c_address': request.GET['adress']
                 }
    return render(request, 'Pizza/order.html', order_data)


def confirm(request):
    c_name = request.GET['c_name']
    p_name = request.GET['pizza_name']
    p_size = request.GET['pizza_size']
    c_address = request.GET['c_address']
    pizza = Pizza.objects.get(name=p_name)
    obj, created = Order.objects.get_or_create(customer_name=c_name,
                                               pizza=pizza,
                                               pizza_size=p_size,
                                               customer_address=c_address)
    print (obj.id)
    return render(request, 'Pizza/final.html', {'id' :obj.id})



def remove(request):
    if request.GET:
        print(request.GET)
        order_id = int(request.GET['hidden_input_order_id'])
        ord_obj = Order.objects.get(id=order_id)
        ord_obj.delete()
    return HttpResponseRedirect(reverse('home'))

