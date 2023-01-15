from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title