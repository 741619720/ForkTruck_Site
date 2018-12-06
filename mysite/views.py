from django.shortcuts import render
from django.shortcuts import HttpResponse
from mysite import  models

# Create your views here.

def Login(request):
    print("=========================")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
    return render(request, "login.html",)

def Task(request):
    if request.method == "POST":
        taskID = request.POST.get("taskID", None)

    task_list = models.RentTaskInfo.objects.all()
    return render(request, "member-list.html", {"data": task_list})

def TaskAdd(request):
    return render(request, "task-add.html")
