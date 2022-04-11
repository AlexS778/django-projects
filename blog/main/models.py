from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20, help_text="post's title")
    body = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title
