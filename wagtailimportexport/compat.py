try:
    from wagtail import hooks
    from wagtail.models import Page
except ImportError:  # fallback for Wagtail < 4.0
    from wagtail.core import hooks
    from wagtail.core.models import Page
except Exception:  # last resort
    from wagtail.wagtailcore import hooks
    from wagtail.wagtailcore.models import Page

try:
    from wagtail.admin import messages
    from wagtail.admin.menu import MenuItem
    from wagtail.admin.widgets import AdminPageChooser

    WAGTAIL_VERSION_2_OR_GREATER = True
except ImportError:  # fallback for Wagtail < 2.0
    from wagtail.wagtailadmin import messages
    from wagtail.wagtailadmin.menu import MenuItem
    from wagtail.wagtailadmin.widgets import AdminPageChooser

    WAGTAIL_VERSION_2_OR_GREATER = False

try:
    from django.utils.translation import (
        ngettext as ngettext,
        gettext as gettext,
        gettext_lazy as gettext_lazy,
    )

except ImportError:  # fallback for Django < 3.0
    from django.utils.translation import (
        ungettext as ngettext,
        ugettext as gettext,
        ugettext_lazy as gettext_lazy,
    )
