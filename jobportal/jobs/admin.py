from django.contrib import admin
from .models import Job
# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):

    list_display = ['title','company_name','salary','location','created_at']

    search_fields = ['title','company_name']

    list_filter = ['location']

    ordering = ['-created_at']