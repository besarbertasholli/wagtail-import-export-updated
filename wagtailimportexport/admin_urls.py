import django

if django.VERSION >= (3, 0):
    from django.urls import re_path as url_path
else:
    from django.conf.urls import url as url_path

from wagtailimportexport import views


app_name = 'wagtailimportexport_admin'
urlpatterns = [
    url_path(r'^import_from_api/$', views.import_from_api, name='import_from_api'),
    url_path(r'^import_from_file/$', views.import_from_file, name='import_from_file'),
    url_path(r'^export_to_file/$', views.export_to_file, name='export_to_file'),
    url_path(r'^$', views.index, name='index'),
]
