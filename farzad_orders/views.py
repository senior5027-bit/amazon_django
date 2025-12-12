from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from product.models import Product
from .models import Order, OrderItem

@login_required
def create_order(request):
    cart = request.session.get('cart', {})

    if not cart:
        return redirect('cart:cart_detail')

    total_price = 0

    order = Order.objects.create(
        user=request.user,
        status='pending',
        total_price=0
    )

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=int(product_id))
        quantity = int(quantity)
        price = product.price

        OrderItem.objects.create(
            order=order,
            product=product,
            price=price,
            quantity=quantity
        )

        total_price += price * quantity

    order.total_price = total_price
    order.save()

    # ❌ cart.clear نکن
    request.session['order_id'] = order.id

    return redirect('cart:payment')
