from django.contrib import admin
from .models import Student,Contact,Course
from .forms import AdminCourseForm
# Register your models here.
admin.site.register(Student)
admin.site.register(Contact)
class CourseAdmin(admin.ModelAdmin):
    form=AdminCourseForm
admin.site.register(Course,CourseAdmin)