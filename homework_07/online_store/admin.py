from django.contrib import admin
from .models import Category, Good, Location, Stock

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Location)
admin.site.register(Stock)

