from django.db import models
from django.contrib.auth.models import User

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_car = models.ForeignKey(..., on_delete=models.CASCADE)
    # tunning = models.ForeignKey(..., on_delete=models.CASCADE)

