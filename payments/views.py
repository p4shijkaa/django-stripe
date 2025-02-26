from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
import logging
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

logger = logging.getLogger(__name__)


def buy_item(request, id):
	item = get_object_or_404(Item, id=id)

	session = stripe.checkout.Session.create(
		payment_method_types=["card"],
		line_items=[
			{
				"price_data": {
					"currency": "usd",
					"product_data": {
						"name": item.name,
						"description": item.description,
					},
					"unit_amount": int(item.price * 100),  # цена в центах
				},
				"quantity": 1,
			}
		],
		mode="payment",
		success_url=request.build_absolute_uri('/success/'),
		cancel_url=request.build_absolute_uri('/cancel/'),
	)
	return JsonResponse({'sessionId': session.id})


def item_detail(request, id):
	item = get_object_or_404(Item, id=id)
	return render(request, 'payments/item_detail.html', {
		'item': item,
		'STRIPE_TEST_PUBLIC_KEY': settings.STRIPE_TEST_PUBLIC_KEY
	})
