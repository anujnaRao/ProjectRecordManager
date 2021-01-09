from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.http import HttpResponse
from .forms import ExtendedFacultyCreationForm, ExtendedStudentCreationForm, ProjectSynopsisForm, ProjectPhase1Form, \
    ProjectPhase2Form, ProjectFinaleForm, TeamCreationForm
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Student, Team, ProjectSynopsis, ProjectPhase1, ProjectPhase2, ProjectFinale


class Homepage(TemplateView):
    template_name = 'index.html'


class StudentDashboard(TemplateView):
    template_name = 'student_dashboard.html'


def facultyDashboard(request):
    queryset1 = Team.objects.filter(guide=request.user.id)
    Doclst = []
    print(queryset1)
    teamId = ""
    for data in queryset1:
        teamId = int(data.id)
        print(teamId)
        queryset2 = ProjectSynopsis.objects.filter(project_title=teamId)

        for dt in queryset2:
            Doclst.append(dt.id)
            print(dt.id)
            print(dt.scrum_master)

    print(Doclst)

    return render(request, 'faculty_dashboard.html', {'team': queryset1, "docx": Doclst})


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
            print(owner)
            print(partner)
            queryset1 = Team.objects.filter(owner=partner)
            # queryset3 = Team.objects.filter(partner=owner)
            # print(queryset1)
            # print(queryset3)
            # for data in queryset3:
            #     print(data.partner)
            #     print(queryset3)
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
            if queryset1:
                messages.error(request, f'Team member already chosen')
                return redirect('teams')
            # if queryset3:
            #     messages.error(request, f'Team member already chosen')
            #     return redirect('teams')
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
    needToUpdate = False
    needToUpdateidt = False

    queryset2 = Team.objects.filter(owner=(request.user.name + " " + request.user.email))
    queryset3 = Team.objects.filter(partner=request.user.id)
    idTitle = ""
    if queryset2:
        for data in queryset3 or queryset2:
            idTitle = int(data.id)
    if queryset3:
        for data in queryset3 or queryset2:
            idTitle = int(data.id)

    queryset = ProjectSynopsis.objects.filter(scrum_master=request.user.name)
    idt = ProjectSynopsis.objects.filter(project_title=idTitle)
    print("==> idt ", idt)
    # print(queryset)
    count = 0
    c1 = 0
    if queryset:
        for data in queryset:
            proj_title = data.project_title
            print("title from Project Syp when come from user.id", data.project_title)
            if data:
                count = count + 1
            if count == 1:
                needToUpdate = True
    if idt:
        for data in idt:
            proj_title = data.project_title
            print("title from Project when title comes from team", data.project_title)
            if data:
                c1 = c1 + 1
            if c1 == 1:
                needToUpdateidt = True
    print(count, c1)
    print(needToUpdate, needToUpdateidt)
    # qs3 =
    if request.method == 'POST':
        formy = ProjectSynopsisForm(request.POST, request.FILES)
        if formy.is_valid():
            formy.save()
            project_title = formy.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectsynopsis')
    else:
        formy = ProjectSynopsisForm()
    return render(request, 'project/project_synopsis.html',
                  {'formy': formy, 'needToUpdate': needToUpdate,
                   'queryset': queryset,
                   'idt': idt,
                   "needToUpdateidt": needToUpdateidt})


class SynopsisUpdateView(UpdateView):
    model = ProjectSynopsis
    template_name = 'project/updateDoc.html'
    fields = ['synopsis']

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Your contact has been successfully created!')
        return redirect('projectsynopsis')


def projectPhase1Creation(request):
    queryset = ProjectPhase1.objects.filter(scrum_master=request.user.name)
    print(queryset)
    count = 0
    needToUpdate = False
    for data in queryset:
        if data:
            count = count + 1
        if count == 1:
            needToUpdate = True
    if request.method == 'POST':
        form1 = ProjectPhase1Form(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            project_title = form1.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectphase1')
    else:
        form1 = ProjectPhase1Form()
    return render(request, 'project/project_phase1.html',
                  {'form1': form1, 'needToUpdate': needToUpdate, 'queryset': queryset})


class Phase1UpdateView(UpdateView):
    model = ProjectPhase1
    template_name = 'project/updatePhase1.html'
    fields = ['phase1']

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Your contact has been successfully created!')
        return redirect('projectphase1')


def projectPhase2Creation(request):
    queryset = ProjectPhase2.objects.filter(scrum_master=request.user.name)
    print(queryset)
    count = 0
    needToUpdate = False
    for data in queryset:
        if data:
            count = count + 1
        if count == 1:
            needToUpdate = True
    if request.method == 'POST':
        form2 = ProjectPhase2Form(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            project_title = form2.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectphase2')
    else:
        form2 = ProjectPhase2Form()
    return render(request, 'project/project_phase2.html',
                  {'form2': form2, 'needToUpdate': needToUpdate, 'queryset': queryset})


class Phase2UpdateView(UpdateView):
    model = ProjectPhase2
    template_name = 'project/updatePhase2.html'
    fields = ['phase2']

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Your contact has been successfully created!')
        return redirect('projectphase2')


def projectFinaleCreation(request):
    queryset = ProjectFinale.objects.filter(scrum_master=request.user.name)
    print(queryset)
    count = 0
    needToUpdate = False
    for data in queryset:
        if data:
            count = count + 1
        if count == 1:
            needToUpdate = True
    if request.method == 'POST':
        formf = ProjectFinaleForm(request.POST, request.FILES)
        if formf.is_valid():
            formf.save()
            project_title = formf.cleaned_data.get('project_title')
            messages.success(request, f'Account created for {project_title}.')
            return redirect('projectfinale')
    else:
        formf = ProjectFinaleForm()
    return render(request, 'project/project_finale.html',
                  {'formf': formf, 'needToUpdate': needToUpdate, 'queryset': queryset})


class FinalUpdateView(UpdateView):
    model = ProjectFinale
    template_name = 'project/updateFinal.html'
    fields = ['finale']

    def form_valid(self, form):
        form.save()
        messages.success(
            self.request, 'Your contact has been successfully created!')
        return redirect('projectfinale')
