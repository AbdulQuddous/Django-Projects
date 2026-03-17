from django.contrib import admin
from . models import Student_data

# Register your models here.
@admin.register(Student_data)
class studentadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email' , 'roll_no')




