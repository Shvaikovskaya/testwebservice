from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import LicenceViewSet, OrganizationViewSet

router_v1 = DefaultRouter()

router_v1.register('v1/licenses',
                   LicenceViewSet,
                   basename='license')

router_v1.register('v1/organizations',
                   OrganizationViewSet,
                   basename='organization')


urlpatterns = [path('', include(router_v1.urls)), ]
