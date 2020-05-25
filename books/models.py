from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(to="books.Author",
                                    verbose_name="authors",
                                    related_name="books")
    short_description = models.TextField()
    published_at = models.DateTimeField()

    class Meta:
        ordering = ["title"]
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return f'Book: {self.title}'


class Author(models.Model):
    first_name = models.CharField(verbose_name="first name", max_length=100)
    last_name = models.CharField(verbose_name="last name", max_length=100)
    about = models.TextField(verbose_name="about", blank=True)
    photo = models.ImageField(verbose_name="photo", blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "author"
        verbose_name_plural = "authors"

    def __str__(self):
        return f'Author: {self.first_name} {self.last_name}'


class Review(models.Model):
    book = models.ForeignKey(to=Book,
                             verbose_name="reviewed book",
                             on_delete=models.CASCADE)
    author = models.CharField(verbose_name="review author", max_length=250)
    content = models.TextField(verbose_name="review content")
    is_recommended = models.BooleanField(verbose_name="I recommend this book")

    class Meta:
        verbose_name = "review"
        verbose_name_plural = "reviews"
