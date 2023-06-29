from django.shortcuts import render, redirect
from .models import Inventory, Order, Transaction
from django.db.models import Sum, Count, Max, F
from .forms import OrderItemForm, InventoryForm, TransactionItemForm, AddItemForm
from django.contrib import messages
from django.conf import settings
import json
from pathlib import Path
# Create your views here.

# home page
def home(request):
    return render(request, 'ims/home.html')

# ims
def dash(request):
    inventory = Inventory.objects.all()
    # total store profit
    totalStoreProfitEarned = inventory.aggregate(
        total_profit_earned=Sum('profit_earned'))['total_profit_earned']
    # total items in stock
    totalItemsInStock = inventory.filter(quantity__gt=0).count()
    # item with highest cost
    itemWithHighestCost = inventory.order_by('-cost').first()
    # item with highest profits
    itemWithHighestProfit = inventory.order_by('-profit').first()
    # item most sold
    itemMostSold = inventory.order_by('-quantity_sold').first()
    # items out of stock
    itemOutOfStock = inventory.filter(quantity=0)
    # item with highest profit earned
    itemWithHighestProfitEarned = inventory.order_by('-profit_earned').first()

    context = {
        'totalStoreProfitEarned': totalStoreProfitEarned,
        'totalItemsInStock': totalItemsInStock,
        'itemWithHighestCost': itemWithHighestCost,
        'itemWithHighestProfit': itemWithHighestProfit,
        'itemMostSold': itemMostSold,
        'itemOutOfStock': itemOutOfStock,
        'itemWithHighestProfitEarned': itemWithHighestProfitEarned
    }
    return render(request, 'ims/dash.html', context)


# inventory
def inventory(request):
    context = {
        'inventorys': Inventory.objects.all()
    }
    return render(request, 'ims/inventory.html', context)

# add item 
def addItem(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            selling_price = form.cleaned_data['selling_price']
            cost = form.cleaned_data['cost']
            if cost > selling_price:
                messages.info(request, "Selling Price less than Cost")
                return redirect('ims-add-item')
                
            form.save()
            return redirect('inventory')
    else:
        form = AddItemForm()

    context ={
        'form': form 
    }
        
    return render(request, 'ims/add_item.html', context)


# item delete 
def itemDelete(request, pk):
    item = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('inventory')
        
    context = {
        'item': item
    }
    return render(request, 'ims/item_delete.html')


# order
def order(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'ims/order.html', context)

# transaction
def transaction(request):
    context = {
        'transactions': Transaction.objects.all()
    }
    return render(request, 'ims/transaction.html', context)


# item
# item list
def item(request):
    context = {
        'items': Inventory.objects.all()
    }
    return render(request, 'ims/item.html', context)

# item details
def viewItem(request, pk):
    item = Inventory.objects.get(id=pk)
    context = {
        'item': item
    }
    return render(request, 'ims/item_details.html', context)

# item edit
def editItem(request, pk):
    item = Inventory.objects.get(id=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        action = request.POST.get('action')
        if action == 'Edit':
            if form.is_valid():
                form.save()
                # messages.success(request, 'Item edited successfully')
                return redirect('ims-view-item', pk)
        elif action == 'Cancel':
            # messages.success(request, 'Item edited successfully')
            return redirect('ims-item')
    else:
        form = InventoryForm(instance=item)

    context = {
        'form': form,
    }
    return render(request, 'ims/edit_item.html', context)

# order placed
def orderPlaced(request, pk):
    item = Inventory.objects.get(id=pk)

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        action = request.POST.get('action')
        if action == 'Accept':
            # print(pk)
            # Update is_received to True
            order.is_received = True
            order.save()

            # Update quantity in Inventory model
            item.quantity += order.quantity
            item.save()

        elif action == 'Reject':
            # Update is_cancel to True
            order.is_cancel = True
            order.save()

    orderPlaced = Order.objects.filter(
        is_received=False, is_cancel=False, item_id=pk)

    context = {
        'orderPlaced': orderPlaced
    }

    #check for new order placed
    if orderPlaced.count() > 0:
        return render(request, 'ims/order_placed.html', context)
    else:
        messages.info(request, "No New Order Placed")
        return redirect('ims-view-item', pk)

# order Received
def orderReceived(request, pk):
    item = Inventory.objects.get(id=pk)
    orderReceived = Order.objects.filter(
        is_received=True, is_cancel=False, name=item.name)
    context = {
        'orderReceived': orderReceived
    }

    # check for order received
    if orderReceived.count() > 0:
        return render(request, 'ims/orders_received.html', context)
    else:
        messages.info(request, "No Order Received")
        return redirect('ims-view-item', pk)

# order Cancelled


def orderCancelled(request, pk):
    item = Inventory.objects.get(id=pk)
    orderCancelled = Order.objects.filter(
        is_received=False, is_cancel=True, name=item.name)
    context = {
        'orderCancelled': orderCancelled
    }

    #check for order cancelled
    if orderCancelled.count() > 0:
        return render(request, 'ims/orders_cancelled.html', context)
    else:
        messages.info(request, "No Order Cancelled")
        return redirect('ims-view-item', pk)

# item sell
def sellItem(request, pk):
    item = Inventory.objects.get(id=pk)
    initial_data = {
        'name': item.name,
        'selling_price': item.selling_price,
    }
    if request.method == 'POST':
        form = TransactionItemForm(request.POST, initial=initial_data)
        if form.is_valid():
            quantity_sold = form.cleaned_data['quantity']

            # check for quantity available to sell
            if quantity_sold > item.quantity:
                messages.info(
                    request, "Quantity entered exceeds available stock")
                return redirect('ims-sell-item', pk=pk)

            transaction = form.save(commit=False)
            transaction.item = item  # Assign the 'item' object to the 'item' field
            transaction.save()

            # Update quantity in Inventory model
            item.quantity -= form.cleaned_data['quantity']
            # Update quantity_sold in Inventory model
            item.quantity_sold += form.cleaned_data['quantity']
            item.save()

            return redirect('transaction')
    else:
        form = TransactionItemForm(initial=initial_data)

    context = {
        'form': form,
    }
    return render(request, 'ims/sell_item.html', context)

# item order


def orderItem(request, pk):
    item = Inventory.objects.get(id=pk)
    initial_data = {
        'name': item.name,
        'cost': item.cost,
    }
    if request.method == 'POST':
        form = OrderItemForm(request.POST, initial=initial_data)
        if form.is_valid():
            order = form.save(commit=False)
            order.item = item  # Assign the 'item' object to the 'item' field
            order.save()
            # product_name = form.cleaned_data.get('name')
            # messages.success(request, f'Order for {product_name} has been placed')
            return redirect('ims-order-placed', pk)

    else:
        form = OrderItemForm(initial=initial_data)

    context = {
        'form': form,
    }
    return render(request, 'ims/order_item.html', context)

# transaction for a particular item
def itemSold(request, pk):
    item =Inventory.objects.get(id=pk)
    itemSold = Transaction.objects.filter(item_id = item)

    context = {
        'transactions' : itemSold
    }
    if itemSold.count() > 0:
        return render(request, 'ims/transaction.html', context)
    else:
        messages.info(request, 'No item sold')
        return redirect('ims-view-item', pk)


    
