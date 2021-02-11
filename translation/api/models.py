from django.db import models


class Translation(models.Model):
  key = models.TextField()
  language = models.TextField()
  phrase = models.TextField(default="")

  class Meta:
    constraints = [
      models.UniqueConstraint(fields=['key', 'language'], name='unique translation')
    ]
