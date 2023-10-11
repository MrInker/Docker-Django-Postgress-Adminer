from django.contrib import admin
from models.models import MainModel


@admin.register(MainModel.MainProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'project_number', 'project_name', 'project_comment',
                    'project_created_date', 'project_created_by',)

    list_filter = ('project_number',)
    search_fields = ('project_number',)
