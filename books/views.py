from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book

def index(request):
    return render(request, "index.html")

def form(request):
    return render(request, "form.html")

def book_list(request):
    books = Book.objects.all()

    context = {
        "books": books
    }

    return render(request, template_name="books.html", context=context)