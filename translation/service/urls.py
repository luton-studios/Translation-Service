from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='service_index'),
    path('<int:pk>/', views.service, name='translation_service'),
]
