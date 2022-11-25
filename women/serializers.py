import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()


def encode():
    model = WomenModel('some title', 'some content')
    model_ser = WomenSerializer(model)
    print(model_ser.data, type(model_ser.data), sep='\n')
    json = JSONRenderer().render(model_ser.data)
    print(json)

def decode():
    stream = io.BytesIO(b'{"title":"some title","content":"some content"}')
    data = JSONParser().parse(stream)
    serializer = WomenSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)

# class WomenSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Women
#         fields = ('title', 'category_id')
#
