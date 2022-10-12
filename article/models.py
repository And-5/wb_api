from django.db import models


class Article(models.Model):
    art = models.PositiveBigIntegerField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    brand = models.CharField(max_length=255, blank=True)


class File(models.Model):
    file = models.FileField(upload_to='excel/')
