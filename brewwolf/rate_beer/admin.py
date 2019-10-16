from django.contrib import admin
from rate_beer.models import Rating, Beer

# Register your models here.
admin.site.register(Rating)
admin.site.register(Beer)
