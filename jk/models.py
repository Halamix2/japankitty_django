from django.db import models

# Create your models here.
class Course(models.Model):
    name_short = models.TextField()
    name = models.TextField()
    course_type = models.TextField(default='none')
    def __str__(self):
        return self.name

