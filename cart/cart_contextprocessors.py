from cart.cart import Cart
from cart.forms import CartAddProductForm


def cart_context(request) -> dict[str: Cart, str: CartAddProductForm]:
    """стоврює форму для об'єкту кошику та його форми"""
    cart_form = CartAddProductForm(initial={'quantity': '1'})
    cart = Cart(request)
    return {'cart': cart, 'cart_form': cart_form}
