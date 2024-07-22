from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Foydalanuvchi modelining qaysi maydonlari admin panelida ko'rsatilishini tanlash
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

# Admin panelga CustomUser modelini qo'shish
admin.site.register(CustomUser, CustomUserAdmin)
