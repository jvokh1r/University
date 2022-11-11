from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account
from .forms import AccountCreationForm, AccountUpdateForm


class AccountAdmin(BaseUserAdmin):
    form = AccountUpdateForm
    add_form = AccountCreationForm
    list_display = ('id', 'username', 'email', 'full_name', 'phone', 'get_role_display', 'image_tag', 'is_superuser',
                    'is_active',
                    'is_staff', 'date_modified', 'date_created')
    readonly_fields = ('date_modified', 'date_created')
    list_filter = ('date_created', 'is_superuser', 'is_staff', 'is_active')
    ordering = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'full_name', 'phone', 'image', 'password', 'role')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('date_modified', 'date_created')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide', ), 'fields': ('username', 'password1', 'password2'), }),
    )
    search_fields = ('username', 'email', 'full_name', 'phone')


admin.site.register(Account, AccountAdmin)
