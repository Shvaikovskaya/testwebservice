from rest_framework import serializers

from licenses.models import Licence
from owners.models import Owner
from repositories.models import Repository


class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Licence
        exclude = ('id',)


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        exclude = ('id',)


class RepositorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Repository
        exclude = ('id',)
