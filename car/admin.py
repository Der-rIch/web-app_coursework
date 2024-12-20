from django.contrib import admin

# Register your models here.
from .models import Car, Body, Discipline, Style, Color, Tunning, Order, OrderStatus

admin.site.register(Car)
admin.site.register(Body)
admin.site.register(Discipline)
admin.site.register(Style)
admin.site.register(Color)
admin.site.register(Tunning)
admin.site.register(Order)
admin.site.register(OrderStatus)
