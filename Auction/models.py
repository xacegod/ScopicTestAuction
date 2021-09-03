from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50, blank=False, unique=True)
    desc = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=False, related_name='%(class)s_seller')
    name = models.CharField(max_length=50, blank=False, unique=True)
    desc = models.TextField(max_length=500, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=None)
    minimum_price = models.IntegerField(blank=True, validators=[MinValueValidator(1)], default=1)
    start = models.DateTimeField(default=timezone.now, null=True)
    end = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=10))
    current_bid = models.IntegerField(default=0)
    item_sold = models.BooleanField(default=False)
    bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_bidder')

    def __str__(self):
        return "Name: %s - Category: %s" % (self.name, self.category.name)


class Bid(models.Model):
    bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='%(class)s_bidder')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, blank=False)
    current_bid = models.IntegerField(default=0)

    def __str__(self):
        return "Name: %s - %s - %s" % (self.item.name, self.bidder.username, self.current_bid)


class UserBalance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    amount = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)

    def __str__(self):
        return "Username: %s - %s" % (self.user.username, self.amount)


class UserBiddingSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, unique=True)
    auto_bid = models.BooleanField(default=False)

    def __str__(self):
        return "Username: %s - %s" % (self.user.username, self.auto_bid)
