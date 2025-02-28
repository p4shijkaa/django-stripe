from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import stripe
from .models import Order

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def create_checkout_session(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    currency = order.items.first().currency

    stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': currency,
                        'product_data': {
                            'name': item.item.name,
                        },
                        'unit_amount': int(item.item.price * 100),
                    },
                    'quantity': item.quantity,
                    'tax_rates': [order.tax.stripe_tax_rate_id] if order.tax else [],
                }
                for item in order.orderitem_set.all()
            ],
            discounts=[{
                'coupon': order.discount.code,
            }] if order.discount else [],
            mode='payment',
            success_url=request.build_absolute_uri('/payments/success/'),
            cancel_url=request.build_absolute_uri('/payments/cancel/'),
        )
        return JsonResponse({'id': session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'payments/item_detail.html', {
        'order': order,
        'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY,
    })


def success_view(request):
    return render(request, 'payments/success.html')


def cancel_view(request):
    return render(request, 'payments/cancel.html')