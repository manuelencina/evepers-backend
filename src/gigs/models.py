from django.db import models

from profiles.models import SellerProfile


class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'subcategories'
        verbose_name = 'SubCategory'
        verbose_name_plural = 'Subcategories'

    def __str__(self):
        return self.name


class Gig(models.Model):
    title = models.CharField(max_length=80, unique=True)
    description = models.TextField()
    review_amount = models.BigIntegerField()
    average_score = models.FloatField()
    gig_picture = models.TextField()
    seller_profile = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'gigs'
        verbose_name = 'Gig'
        verbose_name_plural = 'Gigs'

    def __str__(self):
        return self.title


class Review(models.Model):
    comment = models.TextField()
    score = models.SmallIntegerField()
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
