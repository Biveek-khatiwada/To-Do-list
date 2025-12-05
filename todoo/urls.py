from django.urls import path
from . import views

urlpatterns = [
    
    #add task
    path('addTask/', views.addTask, name='addTask'),
   
   #done task
    path('mark_as_done/<int:pk>/',views.mark_as_done,name='mark_as_done'),
    #undone task
   
    path('mark_as_Undone/<int:pk>/',views.mark_as_Undone,name='mark_as_Undone'),
    
    #edit task
    path('edit_task/<int:pk>/',views.edit_task, name='edit_task'),
    
    #delete task
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
    
]
  