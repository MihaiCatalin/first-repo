from rest_framework import serializers, viewsets
from .models import Card



class CardSerializer(serializers.ModelSerializer):
    #choices= ChoiceSerializer(many=True, read_only=True)
    class Meta:
        model = Card


class CardViewSet(viewsets.ModelViewSet):
	queryset= Card.objects.all()
	serializer_class = CardSerializer