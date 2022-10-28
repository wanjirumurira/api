from django.db import models

# Create your models here.
class MyProfile(models.Model):
    slackUsername = models.CharField(max_length=100)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio= models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.slackUsername
