from django.forms import ModelForm, HiddenInput

from .models import Table, Task

class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['table_name']


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['table', 'task_title', 'task_text']
        widgets = {
            'table': HiddenInput()
        }