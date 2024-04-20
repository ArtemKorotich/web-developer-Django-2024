from django.contrib import admin
from .models import Project, Task, BugReport, FeatureRequest

class BugReportInline(admin.TabularInline):
    model = BugReport
    extra = 0
    fields = ('status',)
    #readonly_fields = ('created_at', 'updated_at')
    #can_delete = True
    #show_change_link = True

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'status', 'project', 'created_at', 'updated_at'] 
    list_filter = ['status','priority', 'project'] 
    search_fields = ['title', 'description'] 
    #fieldsets = [
    #    ('Details', {'fields': ['title', 'description']}),
    #    ('Status', {'fields': ['status']}),
    #]
    ordering = ('created_at',)
    actions = ['change_status_to_fixed']
    def change_status_to_fixed(self, request, queryset):
        queryset.update(status='Fixed')
    change_status_to_fixed.short_description = "Mark selected bug reports as Fixed"
    
 
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin): 
    list_display = ['id', 'title', 'priority', 'project', 'created_at', 'updated_at'] 
    list_filter = ['priority', 'project'] 
    search_fields = ['title', 'description']
    #fieldsets = [
    #    ('Details', {'fields': ['title', 'description']}),
    #    ('Priority', {'fields': ['priority']}),
    #]
    #inlines = [BugReportInline]
    ordering = ('created_at',)