from django.contrib import admin
from .models import Category,Article,Tag,Gbook

# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Tag)
admin.site.register(Gbook)
