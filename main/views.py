from django.http.response import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render

from .models import Book

def index(request):
    return HttpResponse('こんにちは世界')


def temp(request):
    context = {
        'msg': 'こんにちは、世界!!!'
    }
    return render(request, 'main/temp.html', context)

def list(request):
    books = Book.objects.all()
    return render(request, 'main/list.html',{
        'books': books
    })