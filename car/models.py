from django.db import models


class Body(models.Model):
    BodyId = models.IntegerField()
    BodyName = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Car(models.Model):
    CarId = models.IntegerField()
    CarMark = models.CharField(max_length=50)
    CarName = models.CharField(max_length=50)
    ProdYear = models.IntegerField()
    BodyId = models.ForeignKey(Body, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


