from product.models import Products


class Cart(object):

    def __init__(self, request):
        self.request = request
        cart = self.request.session.get('cart')   # Create a Cart Session
        if not cart:
            # save an empty cart in the session
            cart = self.request.session['cart'] = {}
        self.cart = cart

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
            }
        else:
            self.cart[product.id]['quantity'] += 1
        self.cart[product.id]['total_price'] = self.cart[product.id]['quantity'] * product.price
        self.save()

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
        try:
            self.cart[product.id]['quantity'] -= 1
            self.cart[product.id]['total_price'] = self.cart[product.id]['quantity'] * product.price
        except KeyError:
            pass

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
            'total_price': total_price
        }