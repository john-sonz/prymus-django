from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from books.models import Author, Book, Review


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


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"


class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"


class ReviewListView(ListView):
    model = Review
    template_name = "review_list.html"


class ReviewDetailView(DetailView):
    model = Review
    template_name = "review_detail.html"
