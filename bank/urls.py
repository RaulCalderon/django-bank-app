from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, AccountViewSet, TransferViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'transfers', TransferViewSet)

urlpatterns = [
    path('', include(router.urls))
]





