from rest_framework import serializers
from .models import Translation

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Translation
    fields = ('key', 'locale', 'phrase')

