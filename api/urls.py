from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LicenceViewSet, OwnerViewSet, RepositoryViewSet

router_v1 = DefaultRouter()

router_v1.register('v1/licenses',
                   LicenceViewSet,
                   basename='license')

router_v1.register('v1/owners',
                   OwnerViewSet,
                   basename='organization')

router_v1.register('v1/repositories',
                   RepositoryViewSet,
                   basename='repository')


urlpatterns = [path('', include(router_v1.urls)), ]
