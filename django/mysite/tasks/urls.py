from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:table_id>/', views.table, name='table'),
    path('<int:table_id>/<int:task_id>/', views.detail, name='detail'),
]
