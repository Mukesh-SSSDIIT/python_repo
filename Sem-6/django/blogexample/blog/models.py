from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    class Meta:
        db_table = "blog"
