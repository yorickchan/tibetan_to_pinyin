from django.contrib import admin

from app.models import TibetToPinyin


@admin.register(TibetToPinyin)
class TibetToPinyinAdmin(admin.ModelAdmin):
    '''Admin View for TibetToPinyin'''

    list_display = ('tibet', 'pinyin')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)