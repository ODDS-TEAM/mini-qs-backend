from django.db import models

# Create your models here.
class Lesson(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()