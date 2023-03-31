from django.shortcuts import render

from count_data.models import Book, Review

# Create your views here.


def index(request):
    return render(request, 'main.html')


def count(request):
    book_count = Book.objects.count()
    review_count = Review.objects.count()
    context = {
        "book_count": book_count,
        "review_count": review_count
    }
    return render(request, "main.html", context)
