from django.db import models
from car.models import Car
from tunning.models import Tunning
from django.contrib.auth.models import User

class Order(models.Model):
    OrderId = models.IntegerField()
    OrderUser = models.ForeignKey(User, on_delete=models.CASCADE)
    OrderUserCar = models.ForeignKey(Car, on_delete=models.CASCADE)
    OrderTunning = models.ForeignKey(Tunning, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

