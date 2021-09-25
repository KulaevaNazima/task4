from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(Course, CourseAdmin)
admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Contact)
