from django.db import models

class Category(models.Model):
    topic = models.CharField(max_length=100)

    class Meta:
        ordering = ('topic', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.topic


class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    category = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title