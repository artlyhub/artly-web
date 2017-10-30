from django import forms
from items.models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('item',
                  'image',
                  'description',
                  'tags',
                  'status_main',)
