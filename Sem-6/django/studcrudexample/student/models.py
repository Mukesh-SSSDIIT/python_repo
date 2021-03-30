from django.db import models

# Create your models here.
class Student(models.Model):
    studid = models.AutoField()
    studename = models.CharField(20)
    studcity = models.CharField(50)
    class Meta:
        db_table = "stud_data"

class Stream(models.Model):
    stream_id = models.AutoField()
    stream_name = models.CharField(20)
    class Meta:
        db_table = "stream_data"