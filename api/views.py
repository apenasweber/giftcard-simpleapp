from h11 import Response
from rest_framework import viewsets
from rest_framework.response import Response

from .models import GiftCardLogs, GiftCards
from .serializers import GiftCardsLogSerializer, GiftCardsSerializer


class GiftCardsViewSet(viewsets.ModelViewSet):
    queryset = GiftCards.objects.all()
    serializer_class = GiftCardsSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_current_amount = request.data.get("current_amount")
        old_current_amount = instance.current_amount
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if new_current_amount:
            current_amount = old_current_amount - int(new_current_amount)
            instance.current_amount = current_amount
            instance.save()
            GiftCardLogs.objects.create(
                gift_card=instance, used_amount=request.data["current_amount"]
            )

        return Response(serializer.data)
