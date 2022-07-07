from django.conf import settings

from wagtailimportexport import views
from wagtailimportexport.compat import url_path


app_name = 'wagtailimportexport'
urlpatterns = [
    url_path(r'^export/(?P<page_id>\d+)/$', views.export, name='export'),
]

if getattr(settings, "WAGTAILIMPORTEXPORT_EXPORT_UNPUBLISHED", False):
    urlpatterns += urlpatterns + [
        url_path(r'^export/(?P<page_id>\d+)/all/$', views.export, {'export_unpublished': True}, name='export'),
    ]
