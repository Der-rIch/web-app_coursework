from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=20) 


class Style(models.Model):
    name = models.CharField(max_length=20)  


class Color(models.Model):
    name = models.CharField(max_length=20)  
    

class Tunning(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    body_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    disk_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    interer_color = models.ForeignKey(Color, on_delete=models.CASCADE)

