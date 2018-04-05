from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def about(request):
    return HttpResponse('<h1>О нашей компании</h1>')

def hello(request):
    return render(request, 'C:/Users/7878d/PycharmProjects/HELLO/firstapp/templates/index.html', {})