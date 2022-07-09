from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .models import Task
from .forms import TaskForm


# Create your views here.

def home(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'index.html', {'tasks': tasks})


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'index.html'


class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'detail.html'


class TaskEdit(UpdateView):
    model = Task
    template_name = 'cbvedit.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('task:cbvdetail', kwargs={'pk': self.object.id})


class TaskDelete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('task:cbvhome')


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'task': task})


def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task': task})
