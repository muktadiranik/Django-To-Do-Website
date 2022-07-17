from django.shortcuts import render, redirect
from .models import ToDoList
import datetime
from calendar import HTMLCalendar
from .forms import ToDoListForm
from django.contrib import messages


def all_in_one(request):
    # calendar
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    cal = HTMLCalendar().formatmonth(year, month)

    # add item
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.date_added = datetime.datetime.now()
            item.save()
            return redirect("all_in_one")
    else:
        form = ToDoListForm()

    # view to do item list
    if request.user.is_authenticated:
        items = ToDoList.objects.filter(user=request.user)
    else:
        items = []

    return render(request, "all_in_one.html", {
        "calendar": cal,
        "form": form,
        "items": items,
    })


def update_to_do_item(request, item_id):
    item = ToDoList.objects.get(pk=item_id)
    form = ToDoListForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        messages.success(request, "Item Updated!!!")
        return redirect("my_to_do_list")
    return render(request, "update_to_do_item.html", {
        "form": form,

    })


def delete_to_do_item(request, item_id):
    item = ToDoList.objects.get(pk=item_id)
    item.delete()
    messages.success(request, "Item Deleted!!!")
    return redirect("my_to_do_list")


def add_to_do_item(request):
    if request.method == "POST":
        form = ToDoListForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.date_added = datetime.datetime.now()
            item.save()
            return redirect("my_to_do_list")
    else:
        form = ToDoListForm()
    return render(request, "add_to_do_item.html", {
        "form": form,
    })


def my_to_do_list(request):
    items = ToDoList.objects.filter(
        user=request.user.id).order_by("date_added")
    return render(request, "my_to_do_list.html", {
        "items": items,
    })


def home(request):
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    cal = HTMLCalendar().formatmonth(year, month)
    return render(request, "home.html", {
        "calendar": cal,
    })
