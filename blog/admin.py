from django.contrib import admin

# import class with model

from .models import Blog

admin.site.register(Blog)
