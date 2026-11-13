from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404

TASKS = [
    {
        "id": 1,
        "title": "Create Django project",
        "description": "Initialize a new Django project and configure the environment",
        "status": "completed",
        "priority": "high",
        "category": "Django",
    },
    {
        "id": 2,
        "title": "Create Django application",
        "description": "Create a tasks application inside the Django project",
        "status": "completed",
        "priority": "high",
        "category": "Django",
    },
    {
        "id": 3,
        "title": "Configure database",
        "description": "Configure SQLite database connection in Django settings",
        "status": "pending",
        "priority": "high",
        "category": "Database",
    }]

def tasks_list(request):
  return render(request, "tasks/tasks_list.html", context={'tasks':TASKS})

def tasks_about(request):
  return render(request, 'tasks/about.html')

def tasks_detail(request,pk):
  task_detail = None
  for task in TASKS:
     if task['id'] == pk:
        task_detail = task

  if task_detail is None:
      raise Http404('немає такої задачі')

  return render(request, "tasks/tasks_detail.html", context={'task':task_detail})
