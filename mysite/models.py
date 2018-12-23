from django.db import models

# Create your models here.
class RentTaskInfo(models.Model):
    taskID = models.CharField(max_length=32)            #任务号
    forktruckID = models.CharField(max_length=32)       #车辆号
    userName = models.CharField(max_length=32)          #用户名
    userPhone = models.CharField(max_length=32)         #电话
    rent_startDate = models.DateTimeField()             #起租日期
    rent_endDate = models.DateTimeField()               #归还日期
    rent_usedDay = models.IntegerField()                #实际使用天数
    rent_dayPrice = models.FloatField()                 #租价
    rent_transportPrice = models.FloatField()           #运费
    rent_totalPrice = models.FloatField()               #总费用
    rent_securityPrice = models.FloatField()            #押金记录
    rent_selfCost = models.FloatField()                 #供方支出
    attachment = models.FileField()                     #附件
    remark = models.CharField(max_length=200)           #备注

