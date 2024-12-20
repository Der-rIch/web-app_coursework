from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Body(models.Model):
    body_id = models.IntegerField(default=0)
    body_name = models.CharField(max_length=20, default='+')
    def __str__(self):
        return self.body_name

class Discipline(models.Model):
    discipline_id = models.IntegerField(default=0)
    discipline_name = models.CharField(max_length=20, default='+')
    def __str__(self):
        return self.discipline_name

class Style(models.Model):
    style_id = models.IntegerField(default=0)
    style_name = models.CharField(max_length=20, default='+')
    def __str__(self):
        return self.style_name

class OrderStatus(models.Model):
    order_status_id = models.IntegerField(default=0)
    order_status_name = models.CharField(max_length=20, default='+')
    def __str__(self):
        return self.order_status_name 

class Color(models.Model):
    color_id = models.IntegerField(default=0)
    color_name = models.CharField(max_length=20, default='white')
    color_code = models.CharField(max_length=20, default='FFF')
    def __str__(self):
        return self.color_name

class Car(models.Model):
    car_id = models.IntegerField(default=0)
    car_mark = models.CharField(max_length=50, default='+')
    car_name = models.CharField(max_length=50, default='+')
    car_prod_year = models.IntegerField(default=2000)
    car_body_id = models.ForeignKey(Body, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.car_name

class Order(models.Model):
    order_id = models.IntegerField(default=0)
    order_name = models.CharField(max_length=20, default='+')
    order_user_fio = models.CharField(max_length=20, default='+')
    order_user_contact = models.CharField(max_length=20, default='+')
    order_create_date = models.DateTimeField(default=timezone.now)
    order_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    order_car_id = models.ForeignKey(Car, on_delete=models.CASCADE, default=0)
    order_discipline_id = models.ForeignKey(Discipline, on_delete=models.CASCADE, default=0)
    order_style_id = models.ForeignKey(Style, on_delete=models.CASCADE, default=0)
    order_body_color_id = models.ForeignKey(Color, related_name="body_color", on_delete=models.CASCADE, default=0)
    order_disk_color_id = models.ForeignKey(Color, related_name="disk_color", on_delete=models.CASCADE, default=0)
    order_interer_color_id = models.ForeignKey(Color, related_name="interer_color", on_delete=models.CASCADE, default=0)
    order_order_status_id = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.order_name

class Tunning(models.Model):
    tunning_id = models.IntegerField(default=0)
    tunning_name = models.CharField(max_length=20, default='+')
    tunning_discipline_id = models.ForeignKey(Discipline, on_delete=models.CASCADE, default=0)
    tunning_style_id = models.ForeignKey(Style, on_delete=models.CASCADE, default=0)
    tunning_body_color_id = models.ForeignKey(Color, related_name="tunning_body_color", on_delete=models.CASCADE, default=0)
    tunning_disk_color_id = models.ForeignKey(Color, related_name="tunning_disk_color", on_delete=models.CASCADE, default=0)
    tunning_interer_color_id = models.ForeignKey(Color, related_name="tunning_interer_color", on_delete=models.CASCADE, default=0)
    def __str__(self):
        return self.tunning_name

