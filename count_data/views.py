from django.shortcuts import render
from django.db.models import Avg
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


def avg(request):
    books_avg_price = Book.objects.aggregate(Avg('price'))
    # ↓辞書型の値(value)を取り出す方法
    for book_avg_price in books_avg_price.values():
        context = {
            "book_avg_price": book_avg_price
        }
    return render(request, "main.html", context)
