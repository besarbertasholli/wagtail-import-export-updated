import django
from django.conf import settings

if django.VERSION >= (3, 0):
    from django.urls import re_path as url_path
else:
    from django.conf.urls import url as url_path
from wagtailimportexport import views


app_name = 'wagtailimportexport'
urlpatterns = [
    url_path(r'^export/(?P<page_id>\d+)/$', views.export, name='export'),
]

if getattr(settings, "WAGTAILIMPORTEXPORT_EXPORT_UNPUBLISHED", False):
    urlpatterns += urlpatterns + [
        url_path(r'^export/(?P<page_id>\d+)/all/$', views.export, {'export_unpublished': True}, name='export'),
    ]
