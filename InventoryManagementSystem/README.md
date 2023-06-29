# Inventory Management System
IMS (Inventory Management System) is a django application for a business to keep track of its inventory and profits, allowing the owner to order supplies and track sales.

## Tech Stack:
HTML, CSS, Bootstrap, Javascript, Django, MySQL

## Models:
- Inventory
- Orders
- Transaction

## Forms
- Sell Item
- Order Item
- Edit Item
- Add New Item

## Screens:
### 1. Home
Landing Page

### 2. Dashboard 
Statistics: 
- total store profit
- total items in stock
- item with highest cost
- item with highest profits
- item most sold
- items out of stock 
- item with highest profit earned

### 3. Order
Show list of orders with status whether received or cancelled, no action can be performed here 

### 4. Transaction 
Show list of transactions, no action can be performed here 

### 5. Inventory
Show list of items 
- delete button, to delete a item
- add item button, to add a new item
- items list button, to view item details page

### 6. Delete
Show a warning, with choice 'cancel' or 'delete'

### 7. Add Item
Form to add a new item.

### 8. Items List
List of all the items in the Inventory, each item have 
- view button
- edit button
- sell button
- order button

### 9. View 
Show details of an item
- Edit button for making changes to the item 
- Button for showing orders placed, orders received, orders canceled of that item

### 10. Edit 
Form to edit item, form with preload details

### 11. Sell  
Form for selling an item

### 12. Order 
Form for ordering a new item

### 13. Orders:
#### Placed: 
Show list of orders related to a particular item 
- Button to confirm order is received 
- Button to confirm order is canceled

#### Received 
Show list of orders related to a particular item that are successfully received, no action can be performed here

#### Canceled 
Show list of orders related to a particular item that are canceled, no action can be performed here

### 14. Item sold
Transaction for an individual item
