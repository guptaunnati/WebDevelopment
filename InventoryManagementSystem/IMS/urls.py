from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='ims-home'),
    path('ims/', views.dash, name='ims-dash'),
    path('item/', views.item, name='ims-item'),
    path('item/sell/<int:pk>/', views.sellItem, name='ims-sell-item'),
    path('item/edit/<int:pk>/', views.editItem, name='ims-edit-item'),
    path('item/view/<int:pk>/', views.viewItem, name='ims-view-item'),
    path('item/order/<int:pk>/', views.orderItem, name='ims-order-item'),
    path('item/order_placed/<int:pk>/', views.orderPlaced,
         name='ims-order-placed'),
    path('item/order_received/<int:pk>/', views.orderReceived,
         name='ims-order-received'),
    path('item/order_cancelled/<int:pk>/', views.orderCancelled,
         name='ims-order-cancelled'),
    # path('transaction/', views.itemSold, name = 'ims-transaction'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/delete/<int:pk>', views.itemDelete, name = 'ims-delete-item'),
    path('order/', views.order, name='order'),
    path('transaction/', views.transaction, name='transaction'),
    path('inventory/add/', views.addItem, name='ims-add-item'),
    path('transaction/<int:pk>/', views.itemSold, name='ims-sold-item'),

]
