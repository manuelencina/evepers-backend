from django.contrib import admin

from .models import Category, Subcategory, Gig, Review

models = (Category, Subcategory, Gig, Review)

admin.site.register(models)
