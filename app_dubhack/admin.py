from django.contrib import admin

from .models import *

class UserDataModelAdmin(admin.ModelAdmin):
    list_display = ['userID', 'imputShortName', 'imputShortNumber']
    search_fields = ['imputShortNumber', 'imputShortName']

    class Meta:
        model = UserData

class DepartmentModelAdmin(admin.ModelAdmin):
    list_display = [
        'departmentname',
        'departmentshortname',
    ]
    search_fields = [
        'departmentshortname',
        'departmentname',
    ]

    class Meta:
        model = Department

class RequiredCourseModelAdmin(admin.ModelAdmin):
    list_display = [
        'requiredCourseName',
        'requiredCourseNumber',
    ]

    class Meta:
        model = RequiredCourses

class CourseModelAdin(admin.ModelAdmin):
    list_display = [
        'courseid',
        'coursename',
        'coursenumber',
    ]

    search_fields = [
        'coursename',

    ]

    class Meta:
        model = Course

admin.site.register(Course, CourseModelAdin)
admin.site.register(Courseschedule)
admin.site.register(CoursePrecourse)
admin.site.register(Department, DepartmentModelAdmin)
admin.site.register(Quarter)
admin.site.register(RequiredClassForMajor)
admin.site.register(RequiredCourses, RequiredCourseModelAdmin)
admin.site.register(UserData, UserDataModelAdmin)
