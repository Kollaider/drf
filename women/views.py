from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        # lst = Women.objects.all().values()
        # return Response({'posts': list(lst)})
        w = Women.objects.all()
        return Response({'data': WomenSerializer(w, many=True).data})

    def post(self, request):

        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'data': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        instance.delete()

        return Response({"post": "deleted obj " + str(pk)})
