from django.db import models

# Create your models here.
class Transaction_History(models.Model):
    sender = models.TextField(max_length=11)
    receiver = models.TextField(max_length=11)
    amount = models.IntegerField()
