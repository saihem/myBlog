from django.views import generic
from . import models

# Create your views here.

class BlogIndex(generic.ListView):
	queryset= models.Entry.objects.published()
	template_name = "home.html"
	paginate_by = 2

class BlogDetail(generic.DetailView):
	model=models.Entry
	template_name="post.html"

class BlogIndex(generic.ListView):
	template_name = "tasks.html"
	paginate_by= 2