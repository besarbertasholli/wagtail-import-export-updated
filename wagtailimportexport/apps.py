import django
from django.apps import AppConfig

if django.VERSION >= (3, 0):
    from django.utils.translation import gettext_lazy as _
else:
    from django.utils.translation import ugettext_lazy as _


class WagtailImportExportAppConfig(AppConfig):
    name = 'wagtailimportexport'
    label = 'wagtailimportexport'
    verbose_name = _("Wagtail import-export")
