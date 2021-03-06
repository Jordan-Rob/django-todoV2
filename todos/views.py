from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy, reverse
from .models import Todo

# Create your views here.


class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ('title', 'description', 'to_be_done')
    template_name = 'todo_new.html'
    login_url = 'login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todo_list.html'
    login_url = 'login'

    def get_queryset(self):
        qs = Todo.objects.filter(user=self.request.user)
        return qs

    """def dispatch(self, request, *args, **kwargs):
        objects = self.objects.filter(user=self.request.user)
        for obj in objects:
            if obj.user != self.request.user:
                raise PermissionDenied
            return super().dispatch(request, *args, **kwargs)"""


class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo_detail.html'
    login_url = 'login'


class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = ('title', 'description', 'to_be_done')
    template_name = 'todo_edit.html'
    login_url = 'login'


class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('todo_list')
    login_url = 'login'
