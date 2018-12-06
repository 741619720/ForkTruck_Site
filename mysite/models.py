from django.db import models

# Create your models here.
class RentTaskInfo(models.Model):
    taskID = models.CharField(max_length=32)
    forktruckID = models.CharField(max_length=32)
    userName = models.CharField(max_length=32)
    userPhone = models.CharField(max_length=32)
    rent_startDate = models.DateTimeField()
    rent_endDate = models.DateTimeField()
    rent_usedDay = models.IntegerField()
    rent_dayPrice = models.FloatField()
    rent_transportPrice = models.FloatField()
    rent_totalPrice = models.FloatField()
    rent_securityPrice = models.FloatField()            #押金
    rent_selfCost = models.FloatField()                 #供方支出
    attachment = models.FileField()
    remark = models.CharField(max_length=200)           #备注

