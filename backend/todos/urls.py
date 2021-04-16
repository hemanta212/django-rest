from django.urls import path
from .views import DetailTodo, ListTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view(), name='todos'),
    path('', ListTodo.as_view(), name='todos'),
    ]
