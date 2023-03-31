from django.shortcuts import render

from count_data.models import Book

# Create your views here.


def index(request):
    return render(request, 'main.html')


def count(request):
    count = Book.objects.count()
    context = {"count": count}
    return render(request, "main.html", context)
