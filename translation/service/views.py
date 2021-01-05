from django.shortcuts import render
from django.http import HttpResponse
from service.models import Translation

def index(request):
  return HttpResponse("Hello, world. You're at the translation service index.")

def service(request, pk):
  transObj = Translation.objects.get(pk=pk)
  context = {
    "translation": transObj,
  }

  return render(request, "translation.html", context)
