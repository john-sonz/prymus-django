from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def index(request):
    return render(request, "index.html")


def form(request):
    return render(request, "form.html")


def user_profile(request):
    print(request.user)
    return render(request, "profile.html")


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "registration/signup_complete.html")
    else:
        form = UserCreationForm()

    return render(request,
                  "registration/signup_form.html",
                  context={'form': form})


def book_list(request):
    books = Book.objects.all()

    context = {"books": books}

    return render(request, "books.html", context)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)

    context = {"book": book}

    return render(request, "book_detail.html", context)