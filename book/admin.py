from django.contrib import admin

# Register your models here.
from .models import Book,Issue,Rates

admin.site.register(Book)
admin.site.register(Issue)
admin.site.register(Rates)

