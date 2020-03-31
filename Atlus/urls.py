from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from Atlus import views

router = routers.DefaultRouter()
router.register('Atlus', views.PredictView)

urlpatterns = [
    path('', views.predictform, name='atlus'),
    path('status/', views.yesno),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)