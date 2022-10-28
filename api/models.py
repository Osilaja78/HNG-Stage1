from django.db import models

# Create your models here.
class MyDetails(models.Model):
    slackUsername = models.CharField(max_length=30, primary_key=True)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.slackUsername

