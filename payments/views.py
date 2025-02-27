from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    try:
        # Создаем Payment Intent
        intent = stripe.PaymentIntent.create(
            amount=int(item.price * 100),  # Сумма в центах
            currency=item.currency,  # Валюта товара
            payment_method_types=['card'],  # Тип оплаты
            metadata={
                "item_id": item.id,  # Дополнительные данные
                "item_name": item.name,
            },
        )
        return JsonResponse({
            'clientSecret': intent.client_secret,  # Возвращаем client_secret для Stripe.js
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'payments/item_detail.html', {
        'item': item,
        'stripe_public_key': settings.STRIPE_TEST_PUBLIC_KEY,
    })
