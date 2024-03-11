from django.db import models

class People(models.Model):
    people = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()

    def __str__(self):
        return self.people