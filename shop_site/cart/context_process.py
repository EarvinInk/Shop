
from .models import Cart, CartItems
from .views import _cart_id
from django.core.exceptions import ObjectDoesNotExist


def counter(request):
    count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItems.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                count += cart_item.quantity
        except Cart.ObjectDoesNotExist:
            count = 0
    return dict(count=count)
