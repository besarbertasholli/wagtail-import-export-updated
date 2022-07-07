from django.apps import AppConfig
from wagtailimportexport.compat import gettext_lazy as _


class WagtailImportExportAppConfig(AppConfig):
    name = 'wagtailimportexport'
    label = 'wagtailimportexport'
    verbose_name = _("Wagtail import-export")
