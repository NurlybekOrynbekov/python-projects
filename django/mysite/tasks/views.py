from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Table


def index(request):
    table_list = Table.objects.all()
    context = {'table_list': table_list}
    return render(request, 'tasks/index.html', context)


def table(request, table_id):
    table = get_object_or_404(Table, pk=table_id)
    return render(request, 'tasks/table.html', {'table': table})


def detail(request, table_id, task_id):
    return HttpResponse("You're looking at task %s." % task_id)
