from django.shortcuts import render, redirect
from .models import Category, Menu, Table, Waiter, Order, Reception
from .forms import CategoryForm, MenuForm, TableForm, WaiterForm, OrderForm, ReceptionForm


# Create your views here.

# Category Views
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'restaurant/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'restaurant/category_form.html', {'form': form})

def category_update(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'restaurant/category_form.html', {'form': form})

def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'restaurant/category_confirm_delete.html', {'category': category})


# Menu Views
def menu_list(request):
    menus = Menu.objects.all()
    return render(request, 'restaurant/menu_list.html', {'menus': menus})

def menu_create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm()
    return render(request, 'restaurant/menu_form.html', {'form': form})

def menu_update(request, pk):
    menu = Menu.objects.get(pk=pk)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuForm(instance=menu)
    return render(request, 'restaurant/menu_form.html', {'form': form})

def menu_delete(request, pk):
    menu = Menu.objects.get(pk=pk)
    if request.method == 'POST':
        menu.delete()
        return redirect('menu_list')
    return render(request, 'restaurant/menu_confirm_delete.html', {'menu': menu})

# Table Views
def table_list(request):
    tables = Table.objects.all()
    return render(request, 'restaurant/table_list.html', {'tables': tables})

def table_create(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm()
    return render(request, 'restaurant/table_form.html', {'form': form})

def table_update(request, pk):
    table = Table.objects.get(pk=pk)
    if request.method == 'POST':
        form = TableForm(request.POST, instance=table)
        if form.is_valid():
            form.save()
            return redirect('table_list')
    else:
        form = TableForm(instance=table)
    return render(request, 'restaurant/table_form.html', {'form': form})

def table_delete(request, pk):
    table = Table.objects.get(pk=pk)
    if request.method == 'POST':
        table.delete()
        return redirect('table_list')
    return render(request, 'restaurant/table_confirm_delete.html', {'table': table})

# Waiter Views
def waiter_list(request):
    waiters = Waiter.objects.all()
    return render(request, 'restaurant/waiter_list.html', {'waiters': waiters})

def waiter_create(request):
    if request.method == 'POST':
        form = WaiterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waiter_list')
    else:
        form = WaiterForm()
    return render(request, 'restaurant/waiter_form.html', {'form': form})

def waiter_update(request, pk):
    waiter = Waiter.objects.get(pk=pk)
    if request.method == 'POST':
        form = WaiterForm(request.POST, instance=waiter)
        if form.is_valid():
            form.save()
            return redirect('waiter_list')
    else:
        form = WaiterForm(instance=waiter)
    return render(request, 'restaurant/waiter_form.html', {'form': form})

def waiter_delete(request, pk):
    waiter = Waiter.objects.get(pk=pk)
    if request.method == 'POST':
        waiter.delete()
        return redirect('waiter_list')
    return render(request, 'restaurant/waiter_confirm_delete.html', {'waiter': waiter})

# Order Views
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'restaurant/order_form.html', {'form': form})

def order_update(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'restaurant/order_form.html', {'form': form})

def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'restaurant/order_confirm_delete.html', {'order': order})

# Reception Views
def reception_list(request):
    receptions = Reception.objects.all()
    return render(request, 'restaurant/reception_list.html', {'receptions': receptions})

def reception_create(request):
    if request.method == 'POST':
        form = ReceptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reception_list')
    else:
        form = ReceptionForm()
    return render(request, 'restaurant/reception_form.html', {'form': form})

def reception_update(request, pk):
    reception = Reception.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReceptionForm(request.POST, instance=reception)
        if form.is_valid():
            form.save()
            return redirect('reception_list')
    else:
        form = ReceptionForm(instance=reception)
    return render(request, 'restaurant/reception_form.html', {'form': form})

def reception_delete(request, pk):
    reception = Reception.objects.get(pk=pk)
    if request.method == 'POST':
        reception.delete()
        return redirect('reception_list')
    return render(request, 'restaurant/reception_confirm_delete.html', {'reception': reception})



