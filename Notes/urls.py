from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),

    path('', views.home, name='home'),
    path('create/', views.create_todo, name='create_todo'),
    path('current/', views.current_todos, name='current_todos'),
    path('completed/', views.completed_todos, name='completed_todos'),

    path('todo/<int:todo_pk>', views.view_todo, name='view_todo'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='complete_todo'),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name='delete_todo'),

]
