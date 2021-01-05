from django.db import models


class Translation(models.Model):
  key = models.TextField()
  locale = models.TextField()
  phrase = models.TextField()
