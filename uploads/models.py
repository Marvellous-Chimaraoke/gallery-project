from django.db import models

# Create your models here.

class Uploads(models.Model):
    title = models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='images/')
    full_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
