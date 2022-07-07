from wagtailimportexport import views
from wagtailimportexport.compat import url_path


app_name = 'wagtailimportexport_admin'
urlpatterns = [
    url_path(r'^import_from_api/$', views.import_from_api, name='import_from_api'),
    url_path(r'^import_from_file/$', views.import_from_file, name='import_from_file'),
    url_path(r'^export_to_file/$', views.export_to_file, name='export_to_file'),
    url_path(r'^$', views.index, name='index'),
]
