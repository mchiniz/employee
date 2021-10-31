from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'Basemap'
router = DefaultRouter()
router.register('basemap', views.BaseMapViewSet, basename='basemap')

urlpatterns = router.urls
