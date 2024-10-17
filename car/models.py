from django.db import models


class Body(models.Model):
    name = models.CharField(max_length=20)


class Car(models.Model):
    mark = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    yom = models.IntegerField()
    body = models.ForeignKey(Body, on_delete=models.CASCADE)


