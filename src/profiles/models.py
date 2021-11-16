from django.db import models
from accounts.models import Account


class SellerProfile(models.Model):
    profile_picture = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    total_average_score = models.FloatField(blank=True, null=True)
    personal_web_site = models.CharField(max_length=255, blank=True, null=True)
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'seller_profiles'
        verbose_name = 'Seller Profile'
        verbose_name_plural = 'Seller Profiles'

    def __str__(self):
        return '%s' % (self.account.email)
