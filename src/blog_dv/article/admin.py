from django.contrib import admin

from .models import Article, Avater, Category, Tag

admin.site.register(Avater)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
