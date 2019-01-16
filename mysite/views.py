from django.shortcuts import render
from django.shortcuts import HttpResponse
from mysite import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import datetime
import os
import hashlib
import ForkTruck_Site.settings

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

def calc_md5(passwd):
    md5 = hashlib.md5(datetime.datetime.now().encode('utf-8'))
    md5.update(passwd.encode('utf-8'))
    ret = md5.hexdigest()
    return ret

def RenameSaveFile(attachments, taskID):
    i=0
    for filename in attachments:
        temp = os.path.split(filename.name)
        if temp.__len__() < 2:
            m1 = calc_md5(filename.name)
        else:
            m1 = calc_md5(filename.name) + os.path.splitext(temp[1])
        name = os.path.join(taskID, m1)
        destination = open(os.path.join(ForkTruck_Site.settings.MEDIA_ROOT, name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in filename.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        attachments[i] = name
    i = i+1
    return attachments

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
        attachments = request.FILES.getlist("attachment", None)
        remark = request.POST.get("remark", None)

        attachments = RenameSaveFile(attachments, taskID)
        print("rent_startDate:", rent_startDate)
        print("rent_endDate:", rent_endDate)
        print("attachment:", request.FILES)
        models.RentTaskInfo.objects.create(taskID=taskID, forktruckID=forktruckID, userName=userName, userPhone=userPhone, rent_startDate=rent_startDate,
                                           rent_endDate=rent_endDate, rent_usedDay=rent_usedDay, rent_dayPrice=rent_dayPrice, rent_transportPrice=rent_transportPrice,
                                           rent_totalPrice=rent_totalPrice, rent_securityPrice=rent_securityPrice, rent_selfCost=rent_selfCost, attachment=attachments,
                                           remark=remark)

    return render(request, "article-add.html")





def Test(request):
    if request.method == "POST":
        attachments = request.FILES.getlist("img", None)
        print("imgs:", request.FILES)
        print("attachment:", request.FILES.getlist("img", None))
        print("1111", datetime.datetime.now().encode('utf-8'))
        #attachments = RenameSaveFile(attachments, 123)
    return render(request, "test.html")
