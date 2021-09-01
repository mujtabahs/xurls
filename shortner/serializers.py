from rest_framework import serializers, viewsets

from .models import Url

class UrlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Url
        fields = ('link', 'uuid')