from django.db import models


class CustomerModel(models.Model):
    userid = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)


class Upload(models.Model):
    index = models.BigIntegerField(primary_key=True)
    userId = models.BigIntegerField()
    id = models.BigIntegerField()
    title = models.TextField()
    body = models.TextField()

