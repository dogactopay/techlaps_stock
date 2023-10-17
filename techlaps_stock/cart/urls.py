from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='orders')


urlpatterns: list = router.urls
