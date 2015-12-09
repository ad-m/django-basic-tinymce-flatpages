from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django.utils.module_loading import import_string

FLATPAGE_WIDGET = getattr(settings, 'FLATPAGE_WIDGET', 'tinymce.widgets.TinyMCE')

FLATPAGE_WIDGET_KWARGS = getattr(settings, 'FLATPAGE_WIDGET_KWARGS',
                                 {'attrs': {'cols': 100, 'rows': 15}})


class PageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content': import_string(FLATPAGE_WIDGET)(**FLATPAGE_WIDGET_KWARGS),
        }
        fields = '__all__'


class PageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = PageForm

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, PageAdmin)
