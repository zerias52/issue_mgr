from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    list_display = [
        "summary", "reporter", "status", "assignee", "priority",
        "status", "created_on"
    ]

admin.site.register(Issue, IssueAdmin)