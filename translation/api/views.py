# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.settings import api_settings
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework_csv.renderers import CSVRenderer
from .models import Translation
from .serializers import TranslationSerializer


class TranslationViewSet(viewsets.ModelViewSet):
# Returns all translation & by id
  queryset = Translation.objects.all()
  serializer_class = TranslationSerializer
  renderer_classes = (JSONRenderer, BrowsableAPIRenderer, CSVRenderer)
  filterset_fields = ['key', 'language']

  def list(self, request, *args, **kwargs):
    queryset = Translation.objects.all().order_by('key')
    language_params = request.query_params.get('language', None)
    languages = []

    if language_params is not None:
      for language in language_params.split(','):
        languages.append(language)
      
      queryset = queryset.filter(language__in=languages)

    serializer = TranslationSerializer(queryset, many=True)

    return Response(serializer.data)


# pure HTML rendering
# def index(request):
#   return HttpResponse("Hello, world. You're at the translation service index.")

# def service(request, pk):
#   transObj = Translation.objects.get(pk=pk)
#   context = {
#     "translation": transObj,
#   }

#   return render(request, "translation.html", context)
