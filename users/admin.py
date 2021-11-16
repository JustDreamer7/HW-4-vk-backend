from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_filter = ('is_superuser',)
    search_fields = ('company',)


# Register your models here.
admin.site.register(User, UserAdmin)
