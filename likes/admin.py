from django.contrib import admin

from likes.models import ImageLike, ItemLike

admin.site.register(ImageLike)
admin.site.register(ItemLike)
