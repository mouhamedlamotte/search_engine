from django.contrib import admin

from .models import Film, filmGenre

# Register your models here.


admin.site.register(Film)
admin.site.register(filmGenre)
