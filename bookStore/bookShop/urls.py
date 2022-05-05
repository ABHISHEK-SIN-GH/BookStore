from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path('syllabus/', views.syllabus, name="syllabus"),
    path('notes/', views.notes, name="notes"),
    path('manuals/', views.manuals, name="manuals"),
    path('books/', views.books, name="books"),
    path('loginSignup/', views.auth, name="auth"),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]