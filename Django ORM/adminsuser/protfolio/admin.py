from django.contrib import admin
from protfolio.models import Student

# Register your models here.

@admin.register(Student)
class studentadmin(admin.ModelAdmin):
    list_display=('name','age')
    list_filter=('age',)
    search_fields=('name',)
    ordering=('age',)
