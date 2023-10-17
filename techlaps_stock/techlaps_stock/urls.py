from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from cart.models import *
from cart.views import *
from .auth import *


urlpatterns = [
    path('', include("cart.urls"), name='cart'),
    path('admin/', admin.site.urls),
    path('auth/login/', TokenView.as_view()),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
