from django.apps import AppConfig

try:
    from django.utils.translation import gettext_lazy as _
except ImportError:  # fallback for Django < 3.0
    from django.utils.translation import ugettext_lazy as _


class WagtailImportExportAppConfig(AppConfig):
    name = "wagtailimportexport"
    label = "wagtailimportexport"
    verbose_name = _("Wagtail import-export")
