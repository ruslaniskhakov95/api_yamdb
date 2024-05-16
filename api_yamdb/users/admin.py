from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser


class MyUserAdmin(UserAdmin):
    model = MyUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                ('role', 'confirmation_code')
            ),
        }),
    )


admin.site.register(MyUser, MyUserAdmin)
