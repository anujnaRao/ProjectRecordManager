from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class UserManager(BaseUserManager):

    def create_user(self, email, password, is_active=True, is_staff=False, is_superuser=False,
                    is_student=False, is_faculty=False, is_faculty_available=False, is_student_available=False,
                    **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.admin = is_superuser
        user.active = is_active
        user.staff = is_staff
        user.isstudent = is_student
        user.isfaculty = is_faculty
        user.student_available = is_student_available
        user.faculty_available = is_faculty_available
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    first_name = None
    last_name = None
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    isstudent = models.BooleanField(default=False)
    isfaculty = models.BooleanField(default=False)
    student_available = models.BooleanField(default=False)
    faculty_available = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_superuser(self):
        return self.admin

    @property
    def is_student(self):
        return self.isstudent

    @property
    def is_faculty(self):
        return self.isfaculty

    @property
    def is_faculty_available(self):
        return self.faculty_available

    @property
    def is_student_available(self):
        return self.student_available


class Faculty(CustomUser):
    phone = models.CharField(max_length=11, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()

    def __str__(self):
        return self.name + ' ' + self.email

    class Meta:
        db_table = "faculty"


class Batch(models.Model):
    batch_name = models.CharField(max_length=10)

    def __str__(self):
        return self.batch_name


class Student(CustomUser):
    usn = models.CharField(max_length=15, null=True, unique=True, default='1R')
    phone = models.CharField(max_length=11, null=True)
    section = models.CharField(max_length=5, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usn', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.name + ' ' + self.email

    class Meta:
        db_table = "student"


class Team(models.Model):
    owner = models.CharField(max_length=555, unique=True)
    partner = models.OneToOneField(
        Student, on_delete=models.CASCADE, null=True, blank=True, unique= True)
    guide = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=555, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "team"

    def __str__(self):
        return str(self.owner)


class ProjectSynopsis(models.Model):
    project_title = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True)
    synopsis = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_title) + "synopsis"


class ProjectPhase1(models.Model):
    project_title = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True)
    phase1 = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_title) + "phase1"


class ProjectPhase2(models.Model):
    project_title = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True)
    phase2 = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_title) + "phase2"


class ProjectFinale(models.Model):
    project_title = models.ForeignKey(
        Team, on_delete=models.CASCADE, null=True)
    finale = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.project_title) + "finale"
