from django.db import models


class ItemList(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField()
