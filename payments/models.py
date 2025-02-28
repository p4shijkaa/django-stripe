from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	currency = models.CharField(max_length=3, default='usd')

	def __str__(self):
		return self.name


class Order(models.Model):
	items = models.ManyToManyField(Item, through='OrderItem')
	discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True)  # Скидка
	tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True)  # Налог

	def total_price(self):
		return sum(order_item.item.price * order_item.quantity for order_item in self.orderitem_set.all())

	def __str__(self):
		return f"Order {self.id}"


class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return f"{self.quantity} x {self.item.name}"


class Discount(models.Model):
	amount = models.DecimalField(max_digits=5, decimal_places=2)  # Сумма скидки
	code = models.CharField(max_length=50, blank=True, null=True)  # Код скидки

	def __str__(self):
		return f"Скидка {self.amount}%"


class Tax(models.Model):
	rate = models.DecimalField(max_digits=5, decimal_places=2)
	description = models.CharField(max_length=100)
	stripe_tax_rate_id = models.CharField(max_length=100)

	def __str__(self):
		return f"Налог {self.rate}% ({self.description})"
