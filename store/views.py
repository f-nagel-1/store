from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
import random


def store(request):
     #check1 if user is logged in
     # if request.user.is_authenticated:
     #      customer = request.user.customer
     #      # order, created = Order.objects.get_or_create(customer=customer, complete=False)
     #      order = Order.objects.get(customer=customer, complete=False)
     #      #parent is order and orderitem is child and we grab all children with _set.all
     #      items = order.orderitem_set.all()
     #      cartItems = order.get_cart_items
     # else:
     #      items = []
     #      order = {'get_cart_total':0, 'get_cart_items':0}
     #      cartItems = order['get_cart_items']

     # products = Product.objects.all()
     # context = {'products':products, 'cartItems':cartItems}
     # return render(request, 'store/store.html', context)
     return render(request, 'store/store.html')



def books(request):
     #check1 if user is logged in
     if request.user.is_authenticated:
          customer = request.user.customer
          #creating object or querying one with values customer and order status is open
          order, created = Order.objects.get_or_create(customer=customer, complete=False)
          #parent is order and orderitem is child and we grab all children with _set.all
          items = order.orderitem_set.all()
          cartItems = order.get_cart_items
     else:
          items = []
          order = {'get_cart_total':0, 'get_cart_items':0}
          cartItems = order['get_cart_items']

     products = Product.objects.all()
     context = {'products':products, 'cartItems':cartItems}
     return render(request, 'store/books.html', context)




def cart(request):
     #check1 if user is logged in
     if request.user.is_authenticated:
          customer = request.user.customer
          # order, created = Order.objects.get_or_create(customer=customer, complete=False)
          order = Order.objects.get(customer=customer, complete=False)
          #parent is order and orderitem is child and we grab all children with _set.all
          items = order.orderitem_set.all()
          cartItems = order.get_cart_items
          #check2 if user is NOT logged in
     else:
          items = []
          order = {'get_cart_total':0, 'get_cart_items':0}
          cartItems = order['get_cart_items']

     context = {'items':items, 'order':order, 'cartItems':cartItems}
     return render(request, 'store/cart.html', context)



def checkout(request):
     if request.user.is_authenticated:
          customer = request.user.customer
          #creating object or querying one with values customer and order status is open
          # order, created = Order.objects.get_or_create(customer=customer, complete=False)
          order = Order.objects.get(customer=customer, complete=False)
          #parent is order and orderitem is child and we grab all children with _set.all
          items = order.orderitem_set.all()
          cartItems = order.get_cart_items
     else:
          items = []
          order = {'get_cart_total':0, 'get_cart_items':0}
          cartItems = order['get_cart_items']

     context = {'items':items, 'order':order, 'cartItems':cartItems}
     return render(request, 'store/checkout.html', context)

#updateItem for cart page with the + - 
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
     #order as return value
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
     #get or create as a way to update
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was updated', safe=False)



def product(request, obj_id):
    product = Product.objects.get(id=obj_id)
    return render(request,'store/product.html',{'product': product})

def about(request):
     return render(request, 'store/about.html')

def contact(request):
     return render(request, 'store/contact.html')

def success(request):
     if request.method == 'POST':
          neworder = Order()
          neworder.customer = request.user.customer
          neworder.address = request.POST.get('address')
          neworder.city = request.POST.get('city')
          neworder.name = request.POST.get('name')
          neworder.complete = True

          cart = Order.objects.filter(customer=request.user.customer)
         
          # total = 0
          # for item in cart:
          #     total = total + item.product.price * item.product.quantity

          trackno = str(random.randint(11111,99999))
          while Order.objects.filter(transaction_id=trackno) is None:
               trackno = str(random.randint(11111,99999))
          neworder.transaction_id = trackno

          Order.objects.filter(transaction_id=None).delete()
          neworder.save()

          # Order.objects.filter(transaction_id="null").delete()
         
     return render(request, 'store/checkout/success.html')



# def clear(request):
#     cart = Cart(request.session)
#     product = Product.objects.all()
#     cart.clear()
#     return render(request, 'store/books.html')


# def place(request):
# 	transaction_id = datetime.datetime.now().timestamp()
# 	data = json.loads(request.body)
# 	customer = request.user.customer
# 	order, created = Order.objects.get_or_create(customer=customer, complete=True)
# 	total = float(data['form']['total'])
# 	order.transaction_id = transaction_id
# 	order.save()

# 	return JsonResponse('Payment submitted..', safe=False)


