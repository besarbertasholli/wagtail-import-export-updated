from django.urls import re_path
from wagtailimportexport import views


app_name = "wagtailimportexport_admin"
urlpatterns = [
    re_path(r"^import_from_api/$", views.import_from_api, name="import_from_api"),
    re_path(r"^import_from_file/$", views.import_from_file, name="import_from_file"),
    re_path(r"^export_to_file/$", views.export_to_file, name="export_to_file"),
    re_path(r"^$", views.index, name="index"),
]
