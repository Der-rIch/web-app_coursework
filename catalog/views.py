from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h3>Главное<h3>")
def about(request):
    return HttpResponse("<h3>О сайте<h3>")
def contact(request):
    return HttpResponse("<h3>Контакты<h3>")    