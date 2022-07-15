from django.db import transaction

from product.models import Products
from order.models import Orders, OrderDetails


class Cart(object):

    def __init__(self, request):
        self.request = request
        cart = self.request.session.get('cart')   # Create a Cart Session
        if not cart:
            # save an empty cart in the session
            cart = self.request.session['cart'] = {}
        self.cart = cart

    # Dictionary items are ordered, changeable, and does not allow duplicates.
    def add(self, product):
        """
            Add a product to the cart or update its quantity.
        """
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'product_id': product.id,
                'name': product.name,
                'quantity': 1,
                'price': product.price,
                'image': product.image.url if product.image else '',
            }
        else:
            for key, value in self.cart.items():
                if key == str(product.id):
                    if value['quantity'] < product.quantity:
                        value['quantity'] += 1
                        self.save()
                        break
            # self.cart[product.id]['quantity'] += 1  # Not working logical error
        # self.cart[product.id]['total_price'] = self.cart[product.id]['quantity'] * [product.price]
        self.save()

    def session_save(self):
        pass;

    def save(self):
        # update the session cart
        self.request.session['cart'] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.request.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                value['quantity'] -= 1
                if(value['quantity'] < 1):
                    del self.cart[key]
                self.save()
                break
        # try:
        #     self.cart[product.id]['quantity'] -= 1  # Gives error
        #     self.cart[product.id]['total_price'] = self.cart[product.id]['quantity'] * product.price
        # except KeyError:
        #     pass

    def clear(self):
        # empty cart
        self.request.session['cart'] = {}
        self.request.session.modified = True

    def get_total(self):
        total_price = 0
        total_items = 0
        for index, product in self.cart.items():
            total_price += product['quantity'] * product['price']
            total_items += product['quantity']
        return {
            'total_items': total_items,
            'total_price': total_price,
        }

    def save_to_database(self):
        prices = self.get_total()
        order = Orders(name="Custom order", status="Approved", total=prices['total_price'])
        order.save()
        for id, item_detail in self.cart.items():
            product = Products.objects.get(id=id)
            order_detail = OrderDetails()
            order_detail.order = order
            order_detail.product = product
            order_detail.price_each = product.price
            order_detail.quantity = item_detail['quantity']
            product.quantity -= item_detail['quantity']
            product.count_sold += item_detail['quantity']
            order_detail.total_price = product.price * item_detail['quantity']
            order_detail.discount_price = 0
            order_detail.final_price = order_detail.total_price - order_detail.discount_price
            order_detail.save()
            product.save()
        self.clear()
