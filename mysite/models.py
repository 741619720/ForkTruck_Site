from django.db import models
import hashlib
import os

def get_file_path(instance, filenames):
    for filename in filenames:
        temp = os.path.split(filename)
        if temp.count() < 2:
            m1 = hashlib.md5(filename).hexdigest
        else:
            m1 = hashlib.md5(filename).hexdigest + os.path.splitext(temp[1])
        filename = os.path.join("upload", "", m1)
    return filenames


# Create your models here.
class RentTaskInfo(models.Model):
    taskID = models.CharField(max_length=32)                    #任务号
    forktruckID = models.CharField(max_length=32)               #车辆号
    userName = models.CharField(max_length=32)                  #用户名
    userPhone = models.CharField(max_length=32)                 #电话
    rent_startDate = models.DateTimeField()                     #起租日期
    rent_endDate = models.DateTimeField()                       #归还日期
    rent_usedDay = models.IntegerField()                        #实际使用天数
    rent_dayPrice = models.FloatField()                         #租价
    rent_transportPrice = models.FloatField()                   #运费
    rent_totalPrice = models.FloatField()                       #总费用
    rent_securityPrice = models.FloatField()                    #押金记录
    rent_selfCost = models.FloatField()                         #供方支出
    attachment = models.CharField(max_length=1000)              #附件
    remark = models.CharField(max_length=200)                   #备注

    def attachment_list(self):
        return self.attachment.split("/")


class Test(models.Model):
    files = models.CharField(max_length=1000)
