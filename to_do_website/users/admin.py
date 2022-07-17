from django.contrib import admin
from .models import AdditionalUserInfo


@admin.register(AdditionalUserInfo)
class AdditionalUserInfoAdmin(admin.ModelAdmin):
    fields = ("user", "birthday", "address", "zip_code", "phone", "website", "user_image")
    list_display = ("user", "birthday", "address", "zip_code", "phone", "website")
    list_filter = ("user", "birthday", "phone", "zip_code", "website")
    search_fields = ("phone", "birthday")
    ordering = ("user", "birthday")
