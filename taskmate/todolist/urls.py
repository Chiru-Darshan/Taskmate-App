from django.urls import path

from . import views

urlpatterns = [
    path("", views.todoList, name='todoList'),
    path("contact/", views.contact, name='contact'),
    path("about/", views.about, name='about'),
    path('delete/<task_id>', views.delete_task, name="delete_task"),
    path('edit/<task_id>', views.edit_task, name="edit_task"),

]