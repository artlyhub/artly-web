from rest_framework import generics

from items.models import Item
from restapi.ItemDetailPage.serializers import ItemDetailPageSerializer

from utils.paginations import UserResultPagination, StandardResultPagination


class ItemDetailListAPIView(generics.ListAPIView):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemDetailPageSerializer
    pagination_class = StandardResultPagination


class ItemDetailPageAPIView(generics.RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailPageSerializer
