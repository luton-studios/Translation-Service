from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from .views import TranslationViewSet

router = routers.DefaultRouter()
router.register(r'translation', TranslationViewSet)


urlpatterns = [
  # HTML Pages
  # path('', views.index, name='service_index'),
  # path('<int:pk>/', views.service, name='translation_service'),

  # REST API page
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
