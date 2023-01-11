from django.contrib import admin
from .models import Product, Singer, Song, Person, Code, Anime

# Register your models here.

admin.site.register(Product)
admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Person)
admin.site.register(Code)
admin.site.register(Anime)