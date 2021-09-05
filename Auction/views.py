from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Item, Bid, UserBiddingSetting
from django.utils import timezone
from django.http import JsonResponse
import json

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


@login_required(login_url='/login/')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")


@login_required(login_url='/login/')
def item_list(request):
    item_list = Item.objects.filter(start__lt=timezone.now(),
                                    end__gt=timezone.now()).order_by('end', 'name').all()
    page = request.GET.get('page', 1)
    paginator = Paginator(item_list, 10)
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'item_list.html', {'items': items})


@login_required(login_url='/login/')
def item_detail(request, id):
    item = Item.objects.filter(id=id).first()
    if not item:
        return redirect('home')
    return render(request, 'item_detail.html', {'item': item})

@login_required(login_url='/login/')
def bid_for_item(request):
    received_json_data = json.loads(request.body)

    username = received_json_data.get('user')
    item_id = received_json_data.get('item')

    if not username or not item_id:
        return JsonResponse({'Error':'Invalid user or item'})

    user = User.objects.filter(username = username).first()
    item = Item.objects.filter(id= item_id).first()
    if not user or not item:
        return JsonResponse({'Error':'Bad user or item'})
        return redirect('home')

    bid = Bid.objects.create(item=item, user=user, current_bid=item.current_bid + 1)
    bid.save()
    # Get setting from previous bidder if auto bid is activated
    previous = item.userbiddingsetting_set.filter(auto_bid=True, amount__gt=item.current_bid).order_by('-amount').first()
    if previous:
        user = previous.user
        bid = Bid.objects.create(item=item, user=user, current_bid=bid.current_bid + 1)
        bid.save()
        item.current_bid = bid.current_bid
        item.bidder = user
    else:
        item.current_bid = bid.current_bid
        item.bidder = user
    item.save()

    return JsonResponse({'current_bid':bid.current_bid, "user": user.username})