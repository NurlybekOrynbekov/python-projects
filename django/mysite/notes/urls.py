from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.NoteCreate.as_view(), name='create')
]
