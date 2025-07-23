from django.http import HttpResponse


def teste_view(request):
    return HttpResponse("Olá, mundo!")

def index_view(request):
    return HttpResponse("<h1>Olá, mundo!</h1>")