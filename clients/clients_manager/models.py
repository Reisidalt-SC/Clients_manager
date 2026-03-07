from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    packet = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Finishedclient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    tel = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    packet = models.CharField(max_length=100)
    message = models.TextField()
    finished_at = models.DateTimeField(auto_now_add=True)