from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField

from .managers import CustomUserManager, StudentManager, FacultyManager


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Faculty(CustomUser):
    phone = models.CharField(max_length=11, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = FacultyManager()

    def __str__(self):
        return self.name + ' ' + self.email

    class Meta:
        db_table = "faculty"


class Student(CustomUser):
    usn = models.CharField(max_length=15, null=True, unique = True, default='1R')
    phone = models.CharField(max_length=11, null=True)
    section = models.CharField(max_length=5, null=True)
    batch = models.CharField(max_length=5, default='A')
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usn', 'phone']

    objects = StudentManager()

    def __str__(self):
        return self.name + ' ' + self.usn

    class Meta:
        db_table = "student"

class Team(models.Model):
    owner = models.CharField(max_length=555, default = "Name + USN" )
    partner = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    guide = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True, blank=True)
    title =  models.CharField(max_length=555, null = True, unique = True )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "team"

    def __str__(self):
        return self.title + ' '+ self.owner

class Project(models.Model):
    project_title = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    synopsis = HTMLField()
    phase1 = HTMLField()
    phase2 = HTMLField()
    fianle = HTMLField()

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.project_title
