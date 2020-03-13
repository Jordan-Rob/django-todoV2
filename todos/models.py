from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=320)
    to_be_done = models.DateTimeField(null=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])
