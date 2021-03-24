from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

def viewItems(response, id):
    ls = WishList.objects.get(id=id)

    form = TaskForm()

    if response.method == 'POST':
        if response.POST.get("save"):
            for item in ls.task_set.all():
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            
            if len(txt) > 2:
                ls.task_set.create(text=txt, complete=False)
            else:
                print("invalid")
    #     form = TaskForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/')

    context = {'ls':ls, 'form':form}
    return render(response, "tasks/viewItems.html", context)

def updateItem(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/updateItem.html', context)

def deleteItem(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
        
    context = {'item':item}
    return render(request, 'tasks/deleteItem.html', context)

def viewUsers(request):
    displayusername = User.objects.all()
    context = {'displayusername':displayusername}
    return render(request, 'tasks/viewUsers.html', context)

def createList(response):
    if request.method == 'POST':
        form = ListForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            w = WishList(name=n)
            w.save()
            response.user.wishlist.add(w)
        return HttpResponseRedirect("/%i" %w.id)

    else:
        form = ListForm()

    context = {'form':form}
    return render(request, 'tasks/createList.html', context)

def viewLists(response):
    wishlist = WishList.objects
    return render(response, 'tasks/viewLists.html', {'wishlist': wishlist})