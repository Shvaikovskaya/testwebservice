from rest_framework import filters, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import LicenceSerializer, OrganizationSerializer

from licenses.models import Licence
from organizations.models import Organization


@permission_classes((IsAuthenticatedOrReadOnly,))
class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all()
    serializer_class = LicenceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'name': ['iexact'], }

    def get_object(self):
        return get_object_or_404(self.queryset,
                                 key=self.kwargs['key'])


@permission_classes((IsAuthenticatedOrReadOnly,))
class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'login': ['iexact'], }

    def get_object(self):
        return get_object_or_404(self.queryset,
                                 login=self.kwargs['login'])
