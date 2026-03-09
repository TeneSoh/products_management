from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'username', 'phone', 'role','is_active', 'password', 'is_staff')
    list_filter = ('is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('username', 'phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important date'), {'fields': ('last_login', 'date_joined')})
    )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'username', 'phone', 'is_active', 'password', 'is_staff', 'last_name')
    #     })
    # )

    search_fields = ('email', 'username')
    ordering = ('email',)
    # filter_horizontal = ('groups', 'permissions')

admin.site.register(User, CustomUserAdmin)