from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('movies', views.MovieViewSet)
router.register('orders', views.OrderViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls))
]