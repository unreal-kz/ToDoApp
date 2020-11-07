from django.urls import path, include

from .views import index, updateTask, deleteTask

urlpatterns = [
    path ('', index, name = 'home'),
    path ('update/<str:pk>/', updateTask, name = 'update_task'),
    path ('delete/<str:pk>/', deleteTask, name = 'delete_task'),
]



