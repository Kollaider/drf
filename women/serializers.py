import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        # fields = ('title', 'content', 'category')
        fields = '__all__'
