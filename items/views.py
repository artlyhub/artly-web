from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from items.models import Image
from items.forms import ImageForm

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'community.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'community.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('after_upload_show')
    else:
        form = ImageForm()
    return render(request, 'community.html', {
        'form': form
    })

def after_upload_show(request):
    image = Image.objects.order_by('-created').first()
    return render(request, 'after_upload_show.html', {
        'image': image
    })
