import csv, io
from django.shortcuts import render
from django.contrib import messages
from django.db import IntegrityError
# from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_csv.renderers import CSVRenderer
from .models import Translation
from .serializers import TranslationSerializer


class TranslationViewSet(viewsets.ModelViewSet):
  queryset = Translation.objects.all()
  serializer_class = TranslationSerializer
  renderer_classes = (JSONRenderer, BrowsableAPIRenderer, CSVRenderer)
  filterset_fields = ['key', 'language']

  """
  GET call: /api/translation
    query params: 
      - list of keys separated by commas
      - list of languages separated by commas
    response:
      - JSON sample:
        [{
          "key": "items.apple",
          "language": "en",
          "phrase": "Apple",
        }]
      - csv sample:
        key,language,phrase
        items.apple,en,Apple
  """
  def list(self, request, *args, **kwargs):
    queryset = Translation.objects.all().order_by('key')
    language_params = request.query_params.get('language', None)
    key_params = request.query_params.get('key', None)
    languages = []
    keys = []

    if language_params is not None:
      for language in language_params.split(','):
        languages.append(language)
      queryset = queryset.filter(language__in=languages)

    if key_params is not None:
      for key in key_params.split(','):
        keys.append(key)
      queryset = queryset.filter(key__in=keys)

    serializer = TranslationSerializer(queryset, many=True)

    return Response(serializer.data)


# pure HTML rendering

"""
csv Upload endpoint: /api/upload-csv
  csv format:
    key,language,phrase
    items.apple,fr,Pomme de Terre
    items.apple,en,Apple
    items.banana,en,Banana
  response:
    update/create db entries and output
    success or failure message
"""
def upload(request):
  template = "upload.html"
  context = {
    'format': "The header of the csv file should be 'key', 'language', 'phrase'."
  }

  if request.method == "POST":
    csv_file = request.FILES['file']
    
    # validate & decode csv file
    if not csv_file.name.endswith('.csv'):
      messages.error(request, 'ERROR: THIS IS NOT A CSV FILE')
    else:
      data_set = csv_file.read().decode('UTF-8')

      io_string = io.StringIO(data_set)

      # TODO: validate header
      next(io_string)
      # header = csv.reader(next(io_string), delimiter=',', quotechar = '"', skipinitialspace=True)
      # print(header[0], header[1], header[2])
      # if header[0] != 'key' or header[1] != 'language' or header[2] != 'phrase': 
      #   messages.error(request, 'ERROR: CSV FILE HAS THE WRONG FORMAT')
      # else:

      # update/create db entries
      try:
        for column in csv.reader(io_string, delimiter=',', quotechar = '"', skipinitialspace=True):
          obj, created = Translation.objects.update_or_create(
              key=column[0],
              language=column[1],
              defaults={'phrase': column[2]}
          )

          # if entry has been updated, remove all existing translations for other languages
          if not created:
            Translation.objects.filter(key=column[0]).exclude(language=column[1]).update(phrase="")
      except IntegrityError as e:
        messages.success(request,e.message)

      messages.success(request,"SUCCESS: DB has been updated!")

  return render(request, template, context)


# def index(request):
#   return HttpResponse("Hello, world. You're at the translation service index.")

# def service(request, pk):
#   transObj = Translation.objects.get(pk=pk)
#   context = {
#     "translation": transObj,
#   }

#   return render(request, "translation.html", context)
