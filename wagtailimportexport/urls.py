from django.conf import settings
from django.urls import re_path

from wagtailimportexport import views


app_name = "wagtailimportexport"
urlpatterns = [
    re_path(r"^export/(?P<page_id>\d+)/$", views.export, name="export"),
]

if getattr(settings, "WAGTAILIMPORTEXPORT_EXPORT_UNPUBLISHED", False):
    urlpatterns += urlpatterns + [
        re_path(
            r"^export/(?P<page_id>\d+)/all/$",
            views.export,
            {"export_unpublished": True},
            name="export",
        ),
    ]
