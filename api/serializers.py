from rest_framework import serializers

from .models import GiftCardLogs, GiftCards


class GiftCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCards
        fields = "__all__"


class GiftCardsLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCardLogs
        fields = "__all__"
