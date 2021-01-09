from django.urls import path, include
from app import views

urlpatterns = [
    path('', views.Homepage.as_view(), name="index"),
    path('tinymce/', include('tinymce.urls')),
    path('login/', views.Login, name="login"),
    path('facultyRegister/', views.facultyRegistration,
         name="facultyRegistration"),
    path('studentRegister/', views.studentRegistration,
         name="studentRegistration"),
    path('studentdash/', views.StudentDashboard.as_view(), name="studentDashboard"),
    path('facultydash/', views.facultyDashboard, name="facultyDashboard"),
    path('projectsynopsis/', views.projectSynopsisCreation, name="projectsynopsis"),
    path('projectphase1/', views.projectPhase1Creation, name="projectphase1"),
    path('projectphase2/', views.projectPhase2Creation, name="projectphase2"),
    path('projectfianle/', views.projectFinaleCreation, name="projectfinale"),
    path('teams/', views.teamCreation, name="teams"),
    path('projectsynopsis/synopsisUpdate/<int:pk>', views.SynopsisUpdateView.as_view(), name="updateSynopsis"),
    path('projectphase1/phase1Update/<int:pk>', views.Phase1UpdateView.as_view(), name="updatePhase1"),
    path('projectphase2/phase2Update/<int:pk>', views.Phase2UpdateView.as_view(), name="updatePhase2"),
    path('projectfinale/finaleUpdate/<int:pk>', views.FinalUpdateView.as_view(), name="updateFinale"),
    path('logout/', views.logout, name="logout"),
]
