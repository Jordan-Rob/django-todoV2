from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from .models import Todo

# Create your views here.


class TodoCreateView(CreateView):
    model = Todo
    fields = ('title', 'description', 'to_be_done')
    template_name = 'todo_new.html'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TodoListView(ListView):
    model = Todo
    template_name = 'todo_list.html'


class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo_detail.html'


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ('title', 'description', 'to_be_done')
    template_name = 'todo_edit.html'


class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')
