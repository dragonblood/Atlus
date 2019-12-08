from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('Atlus', views.predictView)

urlpatterns = [
    path('', views.predictForm, name='atlus'),
    path('api/', include(router.urls)),
    path('status/', views.approvereject),
]