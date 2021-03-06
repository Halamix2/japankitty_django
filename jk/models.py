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
    sex = models.TextField(null=True, default='unknown')
    surname = models.TextField(null=True)
    birthday = models.DateField(null=True)
    status = models.TextField(default='active')

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.IntegerField()
    #TODO check if this holds true
    category = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
    max_points = models.IntegerField()
