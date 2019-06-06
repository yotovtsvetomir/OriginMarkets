from rest_framework import serializers
from .models import Bond
import requests
import json

class BondSerializer(serializers.ModelSerializer):
    def validate(self, validated_data):
        gleifURL = 'https://leilookup.gleif.org/api/v2/leirecords?lei=' + validated_data['lei']
        resp = requests.get(gleifURL)
        data = json.loads(resp.text)

        if Bond.objects.filter(isin = validated_data['isin']).exists():
            raise serializers.ValidationError('The bond already exists.')
        elif str(data) == '[]':
            raise serializers.ValidationError('The Lei code you have provided is not valid.')
        else:
            validated_data['legal_name'] = data[0]['Entity']['LegalName']['$']
            return validated_data

    class Meta:
        model = Bond
        fields = "__all__"
