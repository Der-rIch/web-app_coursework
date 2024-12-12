from django.db import models


class Body(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Car(models.Model):
    mark = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    yom = models.IntegerField()
    body = models.ForeignKey(Body, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


