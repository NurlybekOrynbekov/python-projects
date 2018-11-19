from django.views import generic
from django.views.generic.edit import FormView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Note
from .forms import NoteForm

class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'notes'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['document_title'] = 'Notes'
        return context

    def get_queryset(self):
        return Note.objects.order_by('-pub_date')


class NoteCreate(FormView):
    template_name = 'notes/create.html'
    form_class = NoteForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
