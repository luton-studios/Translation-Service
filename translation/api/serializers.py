from rest_framework import serializers
from rest_pandas.serializers import PandasSerializer
from .models import Translation

class TranslationSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Translation
    fields = ('key', 'language', 'phrase')


