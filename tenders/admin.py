from django.contrib import admin

from tenders.models import Tenders


class TenderAdmin(admin.ModelAdmin):
    list_filter = ('law',)


# почему-то вылетает из-за ввода
admin.site.register(Tenders, TenderAdmin)
# Register your models here.
