from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=60, null=True)
    short_description = models.TextField()
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title + (" by " + self.author if self.author else "")
