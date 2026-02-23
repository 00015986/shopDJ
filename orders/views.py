from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import Order, OrderItem

@login_required
def order_create(request):                       # Page 4 — Checkout
    cart = Cart(request)
    if request.method == 'POST':
        address = request.POST.get('address', '')
        order = Order.objects.create(user=request.user, address=address)
        for item in cart:
            OrderItem.objects.create(
                order=order, product=item['product'],
                price=item['price'], quantity=item['quantity']
            )
        cart.clear()
        return redirect('orders:detail', pk=order.pk)
    return render(request, 'orders/order_create.html', {'cart': cart})

@login_required
def order_detail(request, pk):                   # Page 5 — Order confirmation
    order = Order.objects.get(pk=pk, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def order_history(request):                      # Page 6 — Order history
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/order_history.html', {'orders': orders})
