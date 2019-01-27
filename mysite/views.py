from django.shortcuts import render
from mysite import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import datetime
import os
import ForkTruck_Site.settings
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponse
from django.core.files import File
from ForkTruck_Site.settings import MEDIA_ROOT as media


def img(request):
    pass

def download(request, filename):
    file_pathname = os.path.join(media, filename)
    with open(file_pathname, 'rb') as f:
        file = File(f)
        response = HttpResponse(file.chunks(), content_type='APPLICATION/OCTET-STREAM')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Length'] = os.path.getsize(file_pathname)
    return response
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

    return render(request, "article-list.html", {"data": task_list})


def MyDateTimeSwitcher(postTime):
    dateTime = postTime.split()
    result = []
    result.extend(dateTime[0].split("-"))
    result.extend(dateTime[1].split(":"))
    return result

# def calc_md5(passwd):
#     md5 = hashlib.md5(datetime.datetime.now().encode('utf-8'))
#     md5.update(passwd.encode('utf-8'))
#     ret = md5.hexdigest()
#     return ret

def mkdir(path):
    import os
    path = path.strip()
    path = path.rstrip("\\")
    if not os.path.exists(path):
        os.makedirs(path)

def RenameSaveFile(attachments, taskID):
    files = ""
    for filename in attachments:
        pathname = os.path.join(ForkTruck_Site.settings.MEDIA_ROOT, taskID)
        mkdir(pathname)
        name = os.path.join(pathname, filename.name)
        destination = open(name, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in filename.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        files += (filename.name+"/")
    print("files---:", files)
    if files.__len__() < 1:
        return None
    return files[:-1]

def EditTask(request, taskID):
    if request.method == "POST":
        task = models.RentTaskInfo.objects.get(taskID=taskID)
        if task == None:
            return None
        else:
            task.forktruckID = request.POST.get("forktruckID", None)
            task.userName = request.POST.get("userName", None)
            task.userPhone = request.POST.get("userPhone", None)
            task.rent_startDate = datetime.datetime.strptime(request.POST.get("rent_startDate", None), '%Y-%m-%d')
            task.rent_endDate = datetime.datetime.strptime(request.POST.get("rent_endDate", None), '%Y-%m-%d')
            task.rent_usedDay = request.POST.get("rent_usedDay", None)
            task.rent_dayPrice = request.POST.get("rent_dayPrice", None)
            task.rent_transportPrice = request.POST.get("rent_transportPrice", None)
            task.rent_totalPrice = request.POST.get("rent_totalPrice", None)
            task.rent_securityPrice = request.POST.get("rent_securityPrice", None)
            task.rent_selfCost = request.POST.get("rent_selfCost", None)
            attachments = request.FILES.getlist("attachment", None)
            task.attachments = RenameSaveFile(attachments, task.taskID)
            task.remark = request.POST.get("remark", None)
            task.save()

            task_list = models.RentTaskInfo.objects.all()
            return render(request, "article-list.html", {"data": task_list})
    else:
        task = models.RentTaskInfo.objects.get(taskID=taskID)
        if task == None:
            return render(request, "article-edit.html")
        else:
            return render(request, "article-edit.html", {"data": task})

def DeleteTask(request, taskID):
    del_task = models.RentTaskInfo.objects.filter(taskID=taskID)
    if del_task:
        del_task.delete()
    task_list = models.RentTaskInfo.objects.all()
    return render(request, "article-list.html", {"data": task_list})



def AddTask(request):
    if request.method == "POST":
        taskID = request.POST.get("taskID", None)
        forktruckID = request.POST.get("forktruckID", None)
        userName = request.POST.get("userName", None)
        userPhone = request.POST.get("userPhone", None)
        rent_startDate = request.POST.get("rent_startDate", None)
        rent_endDate = request.POST.get("rent_endDate", None)
        rent_usedDay = request.POST.get("rent_usedDay", None)
        rent_dayPrice = request.POST.get("rent_dayPrice", None)
        rent_transportPrice = request.POST.get("rent_transportPrice", None)
        rent_totalPrice = request.POST.get("rent_totalPrice", None)
        rent_securityPrice = request.POST.get("rent_securityPrice", None)
        rent_selfCost = request.POST.get("rent_selfCost", None)
        attachments = request.FILES.getlist("attachment", None)
        attachments = RenameSaveFile(attachments, taskID)
        remark = request.POST.get("remark", None)

        print("rent_startDate:", rent_startDate)
        print("rent_endDate:", rent_endDate)
        print("attachment:", request.FILES)
        models.RentTaskInfo.objects.create(taskID=taskID, forktruckID=forktruckID, userName=userName, userPhone=userPhone,
                                           rent_startDate=rent_startDate, rent_endDate=rent_endDate, rent_usedDay=rent_usedDay,
                                           rent_dayPrice=rent_dayPrice, rent_transportPrice=rent_transportPrice,
                                           rent_totalPrice=rent_totalPrice, rent_securityPrice=rent_securityPrice,
                                           rent_selfCost=rent_selfCost, attachment=attachments, remark=remark)

        task_list = models.RentTaskInfo.objects.all()
        return render(request, "article-list.html", {"data": task_list})
    return render(request, "article-add.html")





def Test(request):
    task_list = models.Test.objects.all()
    if request.method == "POST":
        attachments = request.FILES.getlist("img", None)
        print("attachments111:", attachments)
        attachments = RenameSaveFile(attachments, "task1234")
        print("attachments:", attachments)
        models.Test.objects.create(files=attachments)
    return render(request, "test.html", {"images" : attachments})
