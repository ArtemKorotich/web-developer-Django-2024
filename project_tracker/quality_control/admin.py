from django.contrib import admin
from .models import BugReport, FeatureRequest

# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'update_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    ordering = ('created_at',)

# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at', 'update_at')
    list_filter = ('status',  'project')
    search_fields = ('title', 'description')
    ordering = ('created_at',)
    