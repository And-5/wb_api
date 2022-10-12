from django.contrib import admin

from .models import *


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('art', 'name', 'brand')


@admin.register(File)
class ArticleAdmin(admin.ModelAdmin):
    pass
