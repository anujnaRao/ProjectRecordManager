from django.contrib import admin
from .models import CustomUser,Faculty,Student, Team, Project

admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(CustomUser)
admin.site.register(Team)
admin.site.register(Project)
