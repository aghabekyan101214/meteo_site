from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    fields = ['title', 'text', 'image', 'image_tag']
    list_display = ['title', 'text', 'image_tag']
    readonly_fields = ('image_tag', )


admin.site.register(News, NewsAdmin)
