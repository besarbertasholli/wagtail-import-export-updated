# wagtail-import-export-updated

Import/Export for Wagtail CMS pages, images, and documents from CSV, JSON, and API. Forked and updated for usability with new versions of Django/Wagtail, as the original library from Torchbox has not been edited since Apr 2019.
Improvements in functionality, performance, documentation, views, etc will be published time after time.

For a more powerful solution (focused on allowing content to be transferred between multiple instances of a Wagtail project), consider https://github.com/wagtail/wagtail-transfer

A published page and its published descendants can be exported via API or file from a source site and imported into a destination site under an existing page.

The destination site should have the same page models as the source site, with compatible migrations.

## Installation

    pip install wagtail-import-export-updated

Now add to your project's `INSTALLED_APPS`:

    INSTALLED_APPS = [
        # ...
        'wagtailimportexport',
        # ...
    ]

Add the following to your project's urls.py (note that the `include(wagtailimportexport_urls)` line must appear above the `include(wagtail_urls)` line that defines Wagtail's default routes):

    from wagtailimportexport import urls as wagtailimportexport_urls

    urlpatterns = [
        # ...
        url(r'', include(wagtailimportexport_urls)),
        url(r'', include(wagtail_urls)),
    ]

(`wagtailimportexport.urls` contains the export API endpoint. The admin urls are in `wagtailimportexport.admin_urls` and
are automatically registered.)

You should now see an 'Import / Export' item in the Wagtail admin menu.

## Configuration

When importing via the API, only published pages are exported by default. If a descendant page is unpublished it and all its descendants are pruned (even if some of those descendants are themselves published).

It is possible to export all pages under a source page by adding a setting on the source site:

    WAGTAILIMPORTEXPORT_EXPORT_UNPUBLISHED = True

This should _not_ be used in a public source site because the API is unauthenticated and would thus expose unpublished content to anyone.

## Limitations

If the imported content includes any foreign keys to page models, these will be updated to reflect the new page IDs if the target page is also part of the import, or left unchanged otherwise. If the target page is neither part of the import nor does it already exist on the destination site, this is likely to fail with a database integrity error.

Page references within rich text or StreamField content will not be rewritten to reflect new page IDs.

Imports are processed in tree path order; first the base `Page` records are imported, followed by the data for specific page subclasses. If a model is imported which includes a foreign key to a specific subclass of `Page`, and the target page of that foreign key appears in the import but later in tree path order, this will fail with an integrity error (as the relevant record will not have been created at that point).

Non-page data, such as images, documents or snippets, is not included in the import; the user is responsible for ensuring that any objects referenced from imported pages are already present on the destination site (with matching IDs).

## Credits

This project is based on [torchbox/wagtail-import-export](https://github.com/torchbox/wagtail-import-export). Because they use the same Django application name, both cannot be used on the same project at the same time.
