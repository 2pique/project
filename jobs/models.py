from django.db import models

# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,)
    def __str__(self):
        return self.title