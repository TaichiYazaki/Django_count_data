from django.contrib import admin

from count_data.models import Book, Review

# Register your models here.
admin.site.register(Book)
admin.site.register(Review)
