from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('Atlus', views.PredictView)

urlpatterns = [
    path('', views.predictform, name='atlus'),
    path('status/', views.yesno),
]