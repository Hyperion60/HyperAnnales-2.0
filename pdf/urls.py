from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.Error404),
    path('docs/<str:title>', views.views_docs),
    path('zip/<str:annee>/<str:semestre>/<str:matiere>/<str:titre>/', views.download_files),
    path('zip/<str:annee>/<str:matiere>/<str:titre>/', views.Gconfs),
    path('py/<str:annee>/<str:semestre>/<str:matiere>/<str:titre>/', views.print_code_file),
    path('<str:annee>/<str:option>/<str:titre>/', views.views_option),
    path('<str:annee>/<str:semestre>/<str:matiere>/<str:titre>/', views.views_files),
]
