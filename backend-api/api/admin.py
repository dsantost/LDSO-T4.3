from django.contrib import admin
from api import models


class InstitutionAdmin(admin.ModelAdmin):
    def student_count(self, obj):
        return obj.students.count()

    filter_horizontal = ('students',)
    list_display = ('name', 'category', 'higher_up', 'student_count')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'degree')


class EntryGradeAdmin(admin.ModelAdmin):
    list_display = ('value', 'degree')


class EntryGradeInline(admin.TabularInline):
    model = models.EntryGrade
    extra = 3


class DegreeAdmin(admin.ModelAdmin):
    inlines = [EntryGradeInline]


admin.site.register(models.Institution, InstitutionAdmin)
admin.site.register(models.InstitutionAdmin)
admin.site.register(models.City)
admin.site.register(models.Category)
admin.site.register(models.Student)
admin.site.register(models.Comment)
admin.site.register(models.Company)
admin.site.register(models.Subject, SubjectAdmin)
admin.site.register(models.DegreeField)
admin.site.register(models.Degree, DegreeAdmin)
admin.site.register(models.EntryGrade, EntryGradeAdmin)
admin.site.register(models.EntryExam)
admin.site.register(models.Enrollment)
admin.site.register(models.InstitutionHistory)
admin.site.register(models.SkillLevel)
admin.site.register(models.Skill)
admin.site.register(models.Language)
admin.site.register(models.Project)