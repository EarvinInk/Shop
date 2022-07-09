from django.urls import path
from . import views

app_name = 'task'
urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:task_id>/', views.edit, name='edit'),
    path('delete/<int:task_id>/', views.delete, name='delete'),
    path('cbvhome/', views.TaskList.as_view(), name='cbvhome'),
    path('cbvhome/detail/<int:pk>/', views.TaskDetails.as_view(), name='cbvdetail'),
    path('cbvhome/edit/<int:pk>/', views.TaskEdit.as_view(), name='cbvedit'),
    path('cbvhome/delete/<int:pk>/', views.TaskDelete.as_view(), name='cbvdelete')

]
