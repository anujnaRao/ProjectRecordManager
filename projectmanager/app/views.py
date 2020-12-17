from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ExtendedFacultyCreationForm, ExtendedStudentCreationForm, ProjectForm
from django.contrib import messages, auth
from django.shortcuts import render, redirect


class Homepage(TemplateView):
    template_name = 'index.html'


# class Dashboard(TemplateView):
#     template_name = 'student_dashboard.html'


class DashboardFaculty(TemplateView):
    template_name = 'faculty_dashboard.html'


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')

        user = auth.authenticate(email=email, password=pass1)
        if user is not None:
            auth.login(request, user)
            if user.is_student:
                return redirect('projects')
            if user.is_faculty:
                return redirect('facultyDashboard')

        else:
            messages.error(request,
                           'Please enter a correct username and password. Note that both fields may be '
                           'case-sensitive.')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def facultyRegistration(request):
    if request.method == 'POST':
        form = ExtendedFacultyCreationForm(request.POST)
        if form.is_valid():
            form.save()
            ven = form.cleaned_data.get('user')
            print(ven)
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}.')
            return redirect('login')
    else:
        form = ExtendedFacultyCreationForm()
    return render(request, 'faculty_register.html', {'form': form})


def studentRegistration(request):
    if request.method == 'POST':
        form = ExtendedStudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            ven = form.cleaned_data.get('user')
            print(ven)
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}.')
            return redirect('login')
    else:
        form = ExtendedStudentCreationForm()
    return render(request, 'student_register.html', {'forms': form})


# def teamCreation(request):
#     if request.method == 'POST':
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.owner = request.user
#             instance.save()
#
#             project_title = form.cleaned_data.get('project_title')
#             messages.success(request, f'Account created for {project_title}.')
#             return redirect('studentDashboard')
#     else:
#         form = ProjectForm()
#     return render(request, 'student_dashboard.html', {'forms': form})


def projectCreation(request):
    if request.method == 'POST':
        formp = ProjectForm(request.POST, request.FILES)
        if formp.is_valid():
            formp.save()
            project_title = formp.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('studentDashboard')
    else:
        formp = ProjectForm()
    return render(request, 'student_dashboard.html', {'formp': formp})
