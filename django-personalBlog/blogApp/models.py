from django.db import models

# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Post(models.Model):
    date = models.DateField()
    content = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.CASCADE) # El on_delete=models.CASCADE indica que si se elimina una sección, también se eliminarán todos los posts asociados a ella.

    def __str__(self):
        return self.title