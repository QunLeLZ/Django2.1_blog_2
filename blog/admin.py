from django.contrib import admin
from .models import Category,Article,Tag,Gbook
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.

admin.site.register(Category)
admin.site.register(Article, MarkdownxModelAdmin)
admin.site.register(Tag)
admin.site.register(Gbook)
