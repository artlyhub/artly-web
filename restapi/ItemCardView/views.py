from rest_framework import generics

from items.models import Item
from restapi.ItemCardView.serializers import ItemCardSerializer

from utils.paginations import UserResultPagination, StandardResultPagination


class ItemCardListAPIView(generics.ListAPIView):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemCardSerializer
    pagination_class = StandardResultPagination


class ItemCardAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemCardSerializer
