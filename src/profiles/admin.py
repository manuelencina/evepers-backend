from django.contrib import admin

from .models import SellerProfile, SocialNetwork, SellerProfileSocialNetwork

models = (SellerProfile, SocialNetwork, SellerProfileSocialNetwork)

admin.site.register(models)
