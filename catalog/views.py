from django.http import HttpResponse
from .models import Orders
from tunning.models import Tunning

  
def index(request):
    return HttpResponse(f"""
    <h3>Главная страниа</h3>
    <h4>типо инфа</h4>
    """)
def user(request, name ="Undefinded", age =0):
    return HttpResponse(f"""
    <h3>информация о клиенте</h3>
    <h2>Имя: {name} Возраст: {age}</h2>"
    """)
def products(request):
    return HttpResponse("Список услуг")
def contact(request):
    return HttpResponse("<h3>Контакты<h3>")    