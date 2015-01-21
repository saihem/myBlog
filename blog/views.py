from django.views import generic
from django.shortcuts import render
from . import models

# Create your views here.

class BlogIndex(generic.ListView):
	queryset= models.Entry.objects.published()
	template_name = "home.html"
	paginate_by = 2

class BlogDetail(generic.DetailView):
	model=models.Entry
	template_name="post.html"

class BlogTaskIndex(generic.ListView):
	queryset= models.Task.objects.published()
	template_name = "tasks.html"
	paginate_by = 2

class BlogTaskDetail(generic.DetailView):
	model=models.Task
	template_name="taskspost.html"

def tasks(request):
	return render(request, 'tasks.html',)
 	
def about(request):
 	return render(request, 'about.html',)
 

