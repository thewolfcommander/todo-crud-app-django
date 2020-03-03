from django.contrib import admin

from core import models

@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'owner', 'updated', 'active']
    list_filter = ['timestamp', 'owner', 'updated', 'active']