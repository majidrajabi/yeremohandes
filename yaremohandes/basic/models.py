from django.db import models


class EmailForNews(models.Model):
        name = models.CharField(max_length=30)
        email = models.EmailField(max_length=256, unique=True)

        def __str__(self):
            return self.name

class Massage(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    number = models.IntegerField(blank=True, null=True)
    massage = models.TextField()
    def __str__(self):
        return self.first_name
