from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'person'
router = DefaultRouter()
router.register('users', views.UserViewSet, basename='user')
router.register('userprofile', views.UserProfileViewSet, basename='userprofile')

urlpatterns = router.urls
