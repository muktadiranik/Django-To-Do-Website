from django.contrib import admin
from .models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    fields = ["user", "name", "description", "date_added", "date_end", "status"]
    list_display = ["user", "name", "description", "date_added", "date_end", "status"]
    list_filter = ("user", "date_added", "status")
    ordering = ["user", "name"]
    search_fields = ["user", "name"]
