from django.utils.html import format_html
from pkg_resources import parse_version


from django.templatetags.static import static

from wagtail import __version__ as WAGTAIL_VERSION
from wagtail import hooks

def import_wagtailfontawesome_stylesheet():
    return format_html('<link rel="stylesheet" href="{}">',
                       static('wagtailfontawesome/css/wagtailfontawesome.css'))


# New Wagtail versions support importing CSS throughout the admin.
# Fall back to the old hook (editor screen only) for older versions.
if parse_version(WAGTAIL_VERSION) >= parse_version('1.4'):
    admin_stylesheet_hook = 'insert_global_admin_css'
else:
    admin_stylesheet_hook = 'insert_editor_css'

hooks.register(admin_stylesheet_hook, import_wagtailfontawesome_stylesheet)
