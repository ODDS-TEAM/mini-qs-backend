from django.db import models


class Lesson(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f'{self.number} : {self.title}'
