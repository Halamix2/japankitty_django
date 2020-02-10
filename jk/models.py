from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Course(models.Model):
    name_short = models.TextField()
    name = models.TextField()
    course_type = models.TextField(default='none')
    def __str__(self):
        return self.name

class User(AbstractUser):
    #does user want to show their progress to others?
    show_progress = models.BooleanField(default=True)
