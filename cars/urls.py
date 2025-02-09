from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarRecordViewSet

router = DefaultRouter()
router.register(r'car-records', CarRecordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API будет доступен по адресу /api/car-records/
]
