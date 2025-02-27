from django.db import models


class Item(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	price = models.DecimalField(max_digits=8, decimal_places=2)
	currency = models.CharField(max_length=3, default='usd')

	def __str__(self):
		return self.name


class Order(models.Model):
	items = models.ManyToManyField(Item)
	total_price = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return f"Order{self.id}"


class Discount(models.Model):
	order = models.OneToOneField(Order, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=5, decimal_places=2)


class Tax(models.Model):
	order = models.OneToOneField(Order, on_delete=models.CASCADE)
	rate = models.DecimalField(max_digits=5, decimal_places=2)
