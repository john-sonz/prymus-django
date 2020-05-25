from django.urls import path

from books.views import BookListView, book_detail

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='list'),
    path('<int:book_id>/', book_detail, name='detail')
]
