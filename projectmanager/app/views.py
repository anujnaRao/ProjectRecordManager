from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ExtendedFacultyCreationForm, ExtendedStudentCreationForm, ProjectSynopsisForm, ProjectPhase1Form, \
    ProjectPhase2Form, ProjectFinaleForm, TeamCreationForm
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Student, Team


class Homepage(TemplateView):
    template_name = 'index.html'


class StudentDashboard(TemplateView):
    template_name = 'student_dashboard.html'


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')

        user = auth.authenticate(email=email, password=pass1)
        if user is not None:
            auth.login(request, user)
            if user.is_student:
                # queryset = Student.objects.filter(email=email)
                # # print(queryset)
                # # studentDict = {"usn":""}
                # for data in queryset.iterator():
                #     print(data.usn)
                #     print(data.name)
                #     studentDict["usn"] = data.usn
                return redirect('studentDashboard')
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


def teamCreation(request):
    if request.method == 'POST':
        formt = TeamCreationForm(request.POST, request.FILES)
        if formt.is_valid():
            owner = formt.cleaned_data.get('owner')
            partner = formt.cleaned_data.get('partner')
            guide = formt.cleaned_data.get('guide')
            # print(owner)
            queryset1 = Team.objects.filter(owner=partner)
            queryset3 = Team.objects.filter(partner=owner)
            # for data in queryset1:
                # print(data.owner)
            # print(queryset1)
            queryset2 = Team.objects.filter(guide=guide)
            count = 0
            facultyCountExceed = False
            for data in queryset2:
                if data:
                    count = count + 1
                if count >= 6:
                    facultyCountExceed = True
            if str(owner) == str(partner):
                messages.error(request, f'First and Second student cannot be same')
                return redirect('teams')
            if queryset1 or queryset3:
                messages.error(request, f'Team member already chosen')
                return redirect('teams')
            if facultyCountExceed:
                messages.error(request, f'Faculty {guide} is already having 6 teams')
                return redirect('teams')
            else:
                formt.save()
                project_title = formt.cleaned_data.get('title')

                messages.success(request, f'Team created with {partner} with Title: {project_title}.')
                return redirect('teams')
        else:
            messages.error(request, f'Team member already chosen ')
            return redirect('teams')
    else:
        formt = TeamCreationForm()
    return render(request, 'team_create.html', {'formt': formt})


def projectSynopsisCreation(request):
    if request.method == 'POST':
        formy = ProjectSynopsisForm(request.POST, request.FILES)
        if formy.is_valid():
            formy.save()
            project_title = formy.clened_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectsynopsis')
    else:
        formy = ProjectSynopsisForm()
    return render(request, 'project/project_synopsis.html', {'formy': formy})


def projectPhase1Creation(request):
    if request.method == 'POST':
        form1 = ProjectPhase1Form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            project_title = form1.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectphase1')
    else:
        form1 = ProjectPhase1Form()
    return render(request, 'project/project_phase1.html', {'form1': form1})


def projectPhase2Creation(request):
    if request.method == 'POST':
        form2 = ProjectPhase2Form(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            project_title = form2.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectphase2')
    else:
        form2 = ProjectPhase2Form()
    return render(request, 'project/project_phase2.html', {'form2': form2})


def projectFinaleCreation(request):
    if request.method == 'POST':
        formf = ProjectFinaleForm(request.POST, request.FILES)
        if formf.is_valid():
            formf.save()
            project_title = formf.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectfinale')
    else:
        formf = ProjectFinaleForm()
    return render(request, 'project/project_finale.html', {'formf': formf})
