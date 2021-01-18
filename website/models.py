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
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.text