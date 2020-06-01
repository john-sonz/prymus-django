from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView

from books.forms import SimpleForm
from books.models import Author, Book, Review


def index(request):
    return render(request, "index.html")


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
    template_name = "books/book_list.html"


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"


class AuthorListView(ListView):
    model = Author
    template_name = "books/author_list.html"


class ReviewListView(ListView):
    model = Review
    template_name = "books/review_list.html"


class ReviewDetailView(DetailView):
    model = Review
    template_name = "books/review_detail.html"


class SimpleFormView(FormView):
    form_class = SimpleForm
    template_name = "books/simple_form.html"

    def form_valid(self, form):
        ctx = {"name": form.cleaned_data["name"]}
        return render(self.request, "books/simple_form_success.html", ctx)
