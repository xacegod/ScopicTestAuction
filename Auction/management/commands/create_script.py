from Auction.models import Item, Bid, UserBiddingSetting, Category
from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, **options):
        if Category.objects.first():
           return None

        Category.objects.create(name='First Category', desc='First description').save()
        Category.objects.create(name='Second Category', desc='Second description').save()
        category = Category.objects.create(name='Third Category', desc='Third description')
        category.save()

        group = Group.objects.create(name='Default permission group')
        p=Permission.objects.filter(name='Can add bid').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can change bid').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can view bid').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can add category').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can change category').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can view category').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can add item').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can change item').first()
        if p:
            group.permissions.add(p)
        p=Permission.objects.filter(name='Can view item').first()
        if p:
            group.permissions.add(p)

        user = User.objects.create(username='super', email='super@user.com', password='tesT123')
        user.is_superuser = True
        user.save()

        user1 = User.objects.create(username='user1', email='use2r@user.com', password='tesT123')
        user1.is_superuser = False
        user1.groups.add(group)
        user1.save()

        user2 = User.objects.create(username='user2', email='user2@user.com', password='tesT123')
        user2.is_superuser = False
        user2.groups.add(group)
        user2.save()

        for i in range(1, 30):
            item = Item.objects.create(name='Item '+str(i), category=category, seller=user )
            if i % 2 == 1:
                bid = Bid.objects.create(user=user1, item=item, current_bid=1)
                item.bidder = user1
            else:
                bid = Bid.objects.create(user=user2, item=item, current_bid=2)
                item.bidder = user2

            if i % 3 == 1:
                b = UserBiddingSetting.objects.create(item=item, user=bid.user, auto_bid=True, amount=10)
                b.save()

            item.current_bid = bid.current_bid
            item.bidder = bid.user
            bid.save()
            item.save()
