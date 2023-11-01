from django.shortcuts import render
from .models import Section
from django.http import HttpResponseRedirect 

def forumappView(request):
    return render(request, 'todolist.html')

def forumappView(request):
    all_forum_items = Section.objects.all()
    return render(request, 'todolist.html',
    {'all_items':all_forum_items})

def addforumView(request):
    if request.method == "POST":
        name_section = request.POST.get("name_section")
        message = request.POST.get("message")
        comment = request.POST.get("comment")
        new_item = Section(name_section = name_section,message = message, comment = comment)
        new_item.save()
    return HttpResponseRedirect('/forumapp/') 

def deleteForumView(request, i):
    y = Section.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/forumapp/') 


