from django.contrib import admin

from ..models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'last_login')
    readonly_fields = ('last_login', 'password', 'email',)
