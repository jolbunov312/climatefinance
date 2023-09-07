from . import views
from django.urls import path

app_name = 'climatefinance'
urlpatterns = [
    
    path('',views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.ClimatefinanceDetail.as_view(), name='detail'),
    path('project/',views.project, name='project'),
    #add projects
    path('add/', views.CreateProject.as_view(), name='create_project'),
    #about us
    path('about/', views.about_us, name='about_us'),
    #edit projects
    path('update/<int:id>/', views.update_project, name='update_project'),
    #delete a project
    path('delete/<int:id>/', views.delete_project, name='delete_project'),
]