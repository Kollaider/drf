from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women, Category
from women.serializers import WomenSerializer


# class WomenViewSet(viewsets.ReadOnlyModelViewSet):
class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cat = Category.objects.get(pk=pk)
        return Response({'cats': cat.name})
