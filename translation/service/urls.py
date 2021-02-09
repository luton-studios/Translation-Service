from django.urls import include, path
from django.conf.urls import include, url
from rest_framework import routers
from .views import TranslationView

router = routers.DefaultRouter()
router.register(r'translations', TranslationView)

urlpatterns = [
  # path('', views.index, name='service_index'),
  # path('<int:pk>/', views.service, name='translation_service'),
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  # url(r'', TranslationView.as_view()),
]
