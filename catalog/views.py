from django.http import HttpResponse
  
def index(request):
    return HttpResponse("<h3>Главное<h3>")
def about(request, name, age):
    return HttpResponse(f"""
            <h3>О челике</h3>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)
def contact(request):
    return HttpResponse("<h3>Контакты<h3>")    