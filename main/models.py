from django.db import models
from django.utils.html import mark_safe


class News(models.Model):
    title = models.CharField(max_length=190)
    image = models.ImageField(upload_to='main')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
