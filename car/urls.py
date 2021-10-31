from rest_framework.routers import DefaultRouter
from . import views

app_name = 'Car'
router = DefaultRouter()
router.register('car', views.CarViewSet, basename='car')

urlpatterns = router.urls
