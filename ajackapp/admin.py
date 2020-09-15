from django.contrib import admin
from .models import Author,Content,Categories

# Register your models here.
admin.site.register(Author)
admin.site.register(Content)
admin.site.register(Categories)
