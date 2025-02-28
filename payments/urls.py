from django.urls import path
from .views import create_checkout_session, order_detail, success_view, cancel_view

urlpatterns = [
    path('create-checkout-session/<int:order_id>/', create_checkout_session, name='create_checkout_session'),
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
]
