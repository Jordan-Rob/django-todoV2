from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView
)

urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:pk>/detail/', TodoDetailView.as_view(), name='todo_detail'),
    path('<int:pk>/edit/', TodoUpdateView.as_view(), name='todo_edit'),
    path('new/', TodoCreateView.as_view(), name='todo_new'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete')
]
