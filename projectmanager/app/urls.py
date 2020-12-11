from django.urls import path, include
from app import views

urlpatterns = [
    path('',views.Homepage.as_view(), name="index"),
    path('tinymce/', include('tinymce.urls')),
    path('login/',views.LoginPage.as_view(), name="login"),
    path('register/',views.RegisterPage.as_view(), name="register"),
    path('facultyRegister/', views.facultyRegistration, name="facultyRegistration"),
    path('dash/',views.Dashboard.as_view(), name="dash"),
    path('logout/',views.LogoutPage.as_view(), name="logout"),
]