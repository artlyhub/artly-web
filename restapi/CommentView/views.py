from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter

from comments.models import Comment
from restapi.CommentView.serializers import CommentSerializer

from utils.paginations import UserResultPagination, StandardResultPagination


class CommentAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    pagination_class = StandardResultPagination
    filter_backends = [SearchFilter, OrderingFilter]
    list_filter = ['item_type']

    def get_queryset(self, *args, **kwargs):
        queryset = Comment.objects.all()
        query = self.request.GET.get('id')
        search_by = self.request.GET.get('search')
        if query:
            queryset_list = queryset.filter(item__pk=query)
            if search_by and search_by == 'PRF':
                queryset_list = queryset.filter(profile_image__pk=query)
        return queryset_list
