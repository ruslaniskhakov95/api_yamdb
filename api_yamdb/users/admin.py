from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                ('role', 'confirmation_code')
            ),
        }),
    )


admin.site.register(User, MyUserAdmin)
