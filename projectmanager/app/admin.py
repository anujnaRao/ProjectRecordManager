from django.contrib import admin
from .models import CustomUser, Faculty, Student, Team, ProjectSynopsis, ProjectPhase1, ProjectPhase2, ProjectFinale, \
    Batch, Logs


class ConstantValue(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at',)


admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Team, ConstantValue)
admin.site.register(ProjectSynopsis, ConstantValue)
admin.site.register(ProjectPhase1, ConstantValue)
admin.site.register(ProjectPhase2, ConstantValue)
admin.site.register(ProjectFinale, ConstantValue)
admin.site.register(Batch)
admin.site.register(Logs, ConstantValue)
