from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
import uuid
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


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
    slug = models.SlugField(null=True, default=uuid.uuid1)
    tags = TaggableManager()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.text