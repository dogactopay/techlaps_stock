from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='product')
router.register(r'orders', OrderViewSet, basename='orders')
router.register(r'stockmove', StockMoveViewSet, basename='stockmove')


urlpatterns: list = router.urls
