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
    # path('studentdash/', views.Dashboard.as_view(), name="studentDashboard"),
    path('facultydash/', views.DashboardFaculty.as_view(), name="facultyDashboard"),
    path('projects/', views.projectCreation, name="projects"),
    path('logout/', views.logout, name="logout"),
]
