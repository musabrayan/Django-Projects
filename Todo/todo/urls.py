from django.urls import path

from todo import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markAsDone/<int:task_id>/', views.markAsDone, name='markAsDone'),
    path('deleteTodo/<int:task_id>/', views.deleteTodo, name='deleteTodo'),
    path('undoTodo/<int:task_id>/', views.undoTodo, name='undoTodo'),
    path('editTodo/<int:pk>/', views.editTodo, name='editTodo'),
    path('updateTodo/<int:task_id>/', views.updateTodo, name='updateTodo'),
]