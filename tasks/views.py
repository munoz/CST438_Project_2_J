from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import *
from .forms import *

# Create your views here.

def index(request):
    return render(request, 'tasks/home.html')

@login_required
def viewItems(response, id):
    ls = WishList.objects.get(id=id)
    form = TaskForm()
    if response.method == 'POST':
        form = TaskForm(response.POST)
        if form.is_valid():
            n= form.cleaned_data["title"]
            w = Task(title=n, wishlist_id=id)
            w.save()
            
            return redirect('/viewLists')
    context = {'ls':ls, 'form':form}
    return render(response, "tasks/viewItems.html", context)

@login_required
def createList(response):
    if response.method == 'POST':
        form = ListForm(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            w = WishList(name=n)
            w.save()
            response.user.wishlist.add(w)
            
            return redirect("/createList")

    else:
        form = ListForm()

    context = {'form':form}
    return render(response, 'tasks/createList.html', context)

@login_required
def updateItem(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/viewLists')

    context = {'form':form}

    return render(request, 'tasks/updateItem.html', context)

@login_required
def deleteItem(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/viewLists')

    context = {'item':item}
    return render(request, 'tasks/deleteItem.html', context)

@login_required
def deleteUser(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('/viewUsers')

    context = {'user':user}
    return render(request, 'tasks/deleteUser.html', context)

@staff_member_required
def viewUsers(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'tasks/viewUsers.html', context)

@staff_member_required
def adminPage(request):
    return render(request, 'tasks/adminPage.html')



@login_required
def viewLists(response):
    wishlist = WishList.objects
    return render(response, 'tasks/viewLists.html', {'wishlist': wishlist})

@login_required
def deleteList(request, pk):
    print('---------- HEY HEY@@ -----------')
    wishlist = WishList.objects.get(id=pk)

    print(wishlist)
    # wishlist = Wishlist.objects.get(id=pk)

    if request.method == 'POST':
        wishlist.delete()
        return redirect('/viewLists')

    context = {'wishlist':wishlist}
    return render(request, 'tasks/deleteList.html', context)

@login_required
def deleteSelf(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.delete()
        return redirect('/')

    context = {'user':user}
    return render(request, 'tasks/deleteSelf.html', context)
