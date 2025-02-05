from django.db import models

# Create your models here.
#hey i wanted to check if it reflects my repo
class Student(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name
 