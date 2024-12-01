from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Post(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    message = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title