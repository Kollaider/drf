import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women

class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=False)
    time_update = serializers.DateTimeField(read_only=False)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


# class WomenSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Women
#         fields = ('title', 'category_id')
#
