from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=100)
    date = models.DateField()
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.content}'
