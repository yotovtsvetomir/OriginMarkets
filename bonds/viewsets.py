from .models import Bond
from .serializers import BondSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filters
import requests
import json

class BondFilter(filters.FilterSet):
    class Meta:
        model = Bond
        fields = {
            'isin': ['iexact'],
            'size': ['iexact'],
            'currency': ['iexact','icontains'],
            'maturity': ['iexact'],
            'lei': ['iexact'],
            'legal_name': ['icontains']
        }

class BondViewSet(viewsets.ModelViewSet):
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    filterset_class = BondFilter

    @action(methods=['GET'], detail = False)
    def latest(self, request):
        latest = self.get_queryset().order_by('maturity').last()
        serializer = self.get_serializer_class()(latest)
        return Response(serializer.data)
