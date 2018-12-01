from django.db import models

from django.shortcuts import render
from django.http import HttpResponse


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    pizza_size = models.IntegerField()

    def __str__(self):
        return f'{self.name}_{self.pizza_size}'


class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    pizza_size = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name

    def save(self, *args, **kwargs):
        super(Order, self).save(self.customer_name)


