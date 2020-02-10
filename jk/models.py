from django.db import models

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

