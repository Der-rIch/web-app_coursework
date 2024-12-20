from django import forms
from .models import Car, Body, Discipline, Style, Color, Tunning, Order, OrderStatus

class BodyForm(forms.ModelForm):
    class Meta:
        model = Body
        fields = (
            'body_id',
            'body_name'
        )
        
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'car_id',
            'car_mark',
            'car_name',
            'car_prod_year',
            'car_body_id'
        )
        
class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = (
            'discipline_id',
            'discipline_name'
        )

class StyleForm(forms.ModelForm):
    class Meta:
        model = Style
        fields = (
            'style_id',
            'style_name'
        )
        
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = (
            'color_id',
            'color_name',
            'color_code'
        )
        
class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = (
            'order_status_id',
            'order_status_name'
        )
        
class OrderForm(forms.ModelForm):
    #order_create_date = forms.DateField(
    #    label='Дата/время создания заказа',
    #    widget=forms.DateInput(
    #       attrs={'type': 'date'}
    #    )
    #)

    class Meta:
        model = Order
        fields = (
            'order_id',
            'order_name',
            'order_user_fio',
            'order_user_contact',
            'order_user_id',
            'order_car_id',
            'order_discipline_id',
            'order_style_id',
            'order_body_color_id',
            'order_disk_color_id',
            'order_interer_color_id',
            'order_order_status_id',
            'order_create_date'
        )
        labels = {
            'order_id': 'ID заказа',
            'order_name': 'Номер заказа',
            'order_user_fio': 'ФИО заказчика',
            'order_user_contact': 'Контакты заказчика',
            'order_create_date': 'Дата/время создания заказа',
            'order_user_id': 'ID заказчика',
            'order_car_id': 'Марка машины',
            'order_discipline_id': 'Дисциплина тюнинга',
            'order_style_id': 'Стиль',
            'order_body_color_id': 'Цвет кузова',
            'order_disk_color_id': 'Цвет дисков',
            'order_interer_color_id': 'Цвет интерьера',
            'order_order_status_id': 'Статус заказа'
        }
        
class TunningForm(forms.ModelForm):
    class Meta:
        model = Tunning
        fields = (
            'tunning_id',
            'tunning_name',
            'tunning_discipline_id',
            'tunning_style_id',
            'tunning_body_color_id',
            'tunning_disk_color_id',
            'tunning_interer_color_id'
        )
