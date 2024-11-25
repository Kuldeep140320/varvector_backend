from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'level', 'instructor', 'created_at')
    list_filter = ('category', 'level', 'instructor')
    search_fields = ('name', 'description', 'instructor')