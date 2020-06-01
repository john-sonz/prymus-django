from django import forms

from books.models import Book


class SimpleForm(forms.Form):
    name = forms.CharField(label="What's your name?")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []