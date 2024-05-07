from django.db import models

# Create your models here.
# todo/models.py

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
