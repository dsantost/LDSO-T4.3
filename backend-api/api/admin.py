from django.contrib import admin
from api.models import Commentary, City, Category, Company, Subject, Degree, Institution, Student


class InstitutionAdmin(admin.ModelAdmin):
    def student_count(self, obj):
        return obj.students.count()

    filter_horizontal = ('students',)
    list_display = ('name', 'category', 'higher_up', 'student_count')


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree')

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Commentary)
admin.site.register(Company)
admin.site.register(Subject, CourseAdmin)
admin.site.register(Degree)