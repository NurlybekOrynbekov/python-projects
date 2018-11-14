from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect, reverse

from .models import Table, Task
from .forms import TableForm, TaskForm


def index(request):
    table_list = Table.objects.all()
    context = {'table_list': table_list}
    return render(request, 'tasks/index.html', context)


def table(request, table_id):
    table = get_object_or_404(Table, pk=table_id)
    return render(request, 'tasks/table.html', {'table': table})


def detail(request, table_id, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'tasks/task.html', {'task': task})   

def create_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            new_table = form.save()
            return redirect(reverse('tasks:table', args=[new_table.id]))
    else:
        form = TableForm()
    return render(request, 'tasks/create-table.html', {'form': form})


def create_task(request, table_id):
    if request.method == 'POST':
        form = TaskForm(request.POST, initial={'table_id': table_id})
        if form.is_valid():
            new_task = form.save()
            return redirect(reverse('tasks:detail', args=[new_task.table_id, new_task.id]))
    else:
        form = TaskForm(initial={'table': table_id})
    return render(request, 'tasks/create-task.html', {'form': form})