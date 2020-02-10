from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Course(models.Model):
    name_short = models.TextField()
    name = models.TextField()
    course_type = models.TextField(default='none')
    def __str__(self):
        return self.name

class Kanji(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    kanji = models.TextField()
    kunyomi = models.TextField()
    onyomi = models.TextField()
    radicals = models.TextField(null=True)
    definition = models.TextField()
    def __str__(self):
        return self.definition

class Vocabulary(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    kana = models.TextField()
    kanji = models.TextField()
    polish = models.TextField()
    def __str__(self):
        return self.polish

class Text(models.Model):
    offerDescription = models.TextField()
    offerOption1 = models.TextField()
    offerOption2 = models.TextField()
    offerOption3 = models.TextField()
    contactDescription = models.TextField()
    aboutCourse = models.TextField()

class User(AbstractUser):
    #does user want to show their progress to others?
    show_progress = models.BooleanField(default=True)


