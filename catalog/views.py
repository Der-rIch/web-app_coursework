from django.http import HttpResponse
  
def index(request):
    return HttpResponse("Главное")
def index(request):
    return HttpResponse("О сайте")
def index(request):
    return HttpResponse("Контакты")    