from rest_framework import serializers

from licenses.models import Licence
from organizations.models import Organization
from repositories.models import Repository


class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        exclude = ('id',)


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        exclude = ('id',)


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        exclude = ('id',)
