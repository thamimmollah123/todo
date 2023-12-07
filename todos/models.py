from django.db import models

class task(models.Model):
     task=models.CharField(max_length=200)
     is_completed=models.BooleanField(default=False)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now=True)
     
     def __str__(self):
          return self.task
