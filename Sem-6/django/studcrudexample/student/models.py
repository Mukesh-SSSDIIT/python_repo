from django.db import models

# Create your models here.
class Student(models.Model):
    studid = models.IntegerField()
    studename = models.CharField(max_length=20)
    studcity = models.CharField(max_length=50)
    class Meta:
        db_table = "stud_data"

class Stream(models.Model):
    stream_id = models.IntegerField()
    stream_name = models.CharField(max_length=20)
    class Meta:
        db_table = "stream_data"

class Book(models.Model):
    book_id = models.IntegerField()
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_isbn = models.CharField(max_length=20)
    book_publishing_year = models.IntegerField()
    class Meta:
        db_table = "books"