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


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    social_network_links = models.ManyToManyField(
        SellerProfile,
        blank=True,
        through='SellerProfileSocialNetwork'
    )

    class Meta:
        db_table = 'social_networks'
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'

    def __str__(self):
        return self.name


class SellerProfileSocialNetwork(models.Model):
    link = models.TextField()
    seller_profile = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    social_network = models.ForeignKey(
        SocialNetwork,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'seller_profiles_social_networks'
        verbose_name = 'Seller_Profile_Social_Network'
        verbose_name_plural = 'Seller_Profiles_Social_Networks'

    def __str__(self):
        return self.link
