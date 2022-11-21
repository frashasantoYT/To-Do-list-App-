from django.urls import path
from . import views
from . views import DeleteTask

urlpatterns = [
    path('', views.home, name='home'), 
    path('deleteTask/<int:pk>/',DeleteTask.as_view(), name='delete'),
    path('todo-completed/<int:todo_id>/', views.TodoComplete, name='todo-completed'), 
    path('deleteAll/', views.deleteAllTodo, name='DeleteAll'), 
  
]
