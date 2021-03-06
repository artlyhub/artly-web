from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView

from items.views import simple_upload, model_form_upload, after_upload_show

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='test.html'), name='test'),
    url(r'^demo/$', TemplateView.as_view(template_name='index.html'), name='demo'),
    url(r'^upload/$', model_form_upload, name='upload'),
    url(r'^after_upload_show/$', after_upload_show, name='after_upload_show'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('restapi.urls', namespace='api')),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
