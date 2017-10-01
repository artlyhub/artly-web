from rest_framework import generics

from items.models import Item
from restapi.ItemCardView.serializers import ItemCardSerializer


class ItemCardAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCardSerializer
