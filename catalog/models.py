from django.db import models
from car.models import Car
from tunning.models import Tunning
from django.contrib.auth.models import User

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    tunning = models.ForeignKey(Tunning, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

