from rest_framework import filters, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from licenses.models import Licence
from owners.models import Owner
from repositories.models import Repository

from . import serializers


@permission_classes((IsAuthenticatedOrReadOnly,))
class LicenceViewSet(viewsets.ModelViewSet):
    queryset = Licence.objects.all()
    serializer_class = serializers.LicenceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'name': ['iexact'], }

    def get_object(self):
        return get_object_or_404(self.queryset,
                                 key=self.kwargs['key'])


@permission_classes((IsAuthenticatedOrReadOnly,))
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = serializers.OwnerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'login': ['iexact'], }

    def get_object(self):
        return get_object_or_404(self.queryset,
                                 login=self.kwargs['login'])


@permission_classes((IsAuthenticatedOrReadOnly,))
class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = serializers.RepositorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'name': ['iexact'], }

    def get_object(self):
        return get_object_or_404(self.queryset,
                                 fill_name=self.kwargs['full_name'])
