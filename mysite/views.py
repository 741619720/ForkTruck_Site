from django.shortcuts import render
from django.shortcuts import HttpResponse
from mysite import  models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import datetime

# Create your views here.

def Login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    username = request.POST['username']
    password = request.POST['password']
    #User.objects.create_user(username=username, password=password)
    user = authenticate(username=username, password=password)
    print(user)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return Task(request)
            # return reverse('index')
        else:
            return render(request, 'login.html', {'errmsg': 'disabled account'})
            # Return a 'disabled account' error message
    else:
        return render(request, 'login.html', {'errmsg': 'invalid login'})


def Task(request):
    task_list = models.RentTaskInfo.objects.all()
    print("task_list:", task_list)
    return render(request, "article-list.html", {"data": task_list})


def MyDateTimeSwitcher(postTime):
    dateTime = postTime.split()
    result = []
    result.extend(dateTime[0].split("-"))
    result.extend(dateTime[1].split(":"))
    return result

def AddTask(request):
    if request.method == "POST":
        taskID = request.POST.get("taskID", None)
        forktruckID = request.POST.get("forktruckID", None)
        userName = request.POST.get("userName", None)
        userPhone = request.POST.get("userPhone", None)
        rent_startDate = datetime.datetime.strptime(request.POST.get("rent_startDate", None), '%Y-%m-%d')
        rent_endDate = datetime.datetime.strptime(request.POST.get("rent_endDate", None), '%Y-%m-%d')
        rent_usedDay = request.POST.get("rent_usedDay", None)
        rent_dayPrice = request.POST.get("rent_dayPrice", None)
        rent_transportPrice = request.POST.get("rent_transportPrice", None)
        rent_totalPrice = request.POST.get("rent_totalPrice", None)
        rent_securityPrice = request.POST.get("rent_securityPrice", None)
        rent_selfCost = request.POST.get("rent_selfCost", None)
        attachment = request.FILES.get("attachment", None)
        remark = request.POST.get("remark", None)

        print("rent_startDate:", rent_startDate)
        print("rent_endDate:", rent_endDate)
        print("attachment:", attachment)
        models.RentTaskInfo.objects.create(taskID=taskID, forktruckID=forktruckID, userName=userName, userPhone=userPhone, rent_startDate=rent_startDate,
                                           rent_endDate=rent_endDate, rent_usedDay=rent_usedDay, rent_dayPrice=rent_dayPrice, rent_transportPrice=rent_transportPrice,
                                           rent_totalPrice=rent_totalPrice, rent_securityPrice=rent_securityPrice, rent_selfCost=rent_selfCost, attachment=attachment,
                                           remark=remark)

    return render(request, "article-add.html")

def Test(request):
    if request.method == "POST":
        attachment = request.FILES.get("img", None)
        print("attachment:", request.FILES)
    return render(request, "test.html")
