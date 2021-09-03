from django.contrib import admin
from .models import Item, Category, Bid, UserBiddingSetting, UserBalance

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    fields = ('seller_id', 'name', 'desc', 'category', 'minimum_price', 'start', 'end', 'item_sold')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    pass

@admin.register(UserBalance)
class UserBalanceAdmin(admin.ModelAdmin):
    pass

@admin.register(UserBiddingSetting)
class UserBiddingSettingAdmin(admin.ModelAdmin):
    pass