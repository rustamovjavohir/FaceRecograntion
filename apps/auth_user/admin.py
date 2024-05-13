from django.contrib import admin
from apps.auth_user.models import User, Staff


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('-is_staff', '-is_superuser', '-is_active')
    fieldsets = (
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'profile_photo')}),
        (None, {'fields': ('username', 'password')}),
        ('Разрешения', {'fields': ('groups', 'user_permissions')}),
        ('Роль пользователя', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Информация о дате', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'phone', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups',)}),

    )
    readonly_fields = ('full_name', 'last_login', 'date_joined')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'department', 'telegram_id')
