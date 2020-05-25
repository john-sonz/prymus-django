"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from books import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.user_profile, name='user_profile'),
    path('accounts/signup/', views.user_signup, name="user_signup"),
    path('form/', views.form, name='form'),
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('authors/', views.AuthorListView.as_view(), name="authors_list"),
    path('reviews/', views.ReviewListView.as_view(), name="reviews_list"),
    path('reviews/<int:pk>/',
         views.ReviewDetailView.as_view(),
         name="review_detail")
]
