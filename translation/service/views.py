from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_pandas import PandasView
from service.models import Translation
from service.serializers import TranslationSerializer


# class TranslationView(PandasView):
class TranslationView(viewsets.ModelViewSet):
  queryset = Translation.objects.all()
  serializer_class = TranslationSerializer


def index(request):
  return HttpResponse("Hello, world. You're at the translation service index.")

def service(request, pk):
  transObj = Translation.objects.get(pk=pk)
  context = {
    "translation": transObj,
  }

  return render(request, "translation.html", context)
