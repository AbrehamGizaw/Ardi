from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with additional fields."""
    model = CustomUser

    # Override fieldsets to include your custom fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('firstname', 'lastname', 'phone', 'gender', 'status', 'profile')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'created_date')}),
    )
    
    # Override add_fieldsets to include your custom fields
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'firstname', 'lastname', 'phone', 'gender'),
        }),
    )

    list_display = ('email', 'firstname', 'lastname', 'is_staff', 'phone', 'gender', 'status')
    search_fields = ('email', 'firstname', 'lastname', 'phone')
    ordering = ('email',)

# Unregister the default User model and register the CustomUser model
admin.site.unregister(get_user_model())
admin.site.register(CustomUser, CustomUserAdmin)
