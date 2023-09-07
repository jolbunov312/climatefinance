from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from django.template import loader
from .forms import ProjectForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    project_list = Project.objects.all()
    context = {
        'project_list':project_list,
    }
    return render(request, 'climatefinance/index.html', context)


class IndexClassView(ListView):
    model = Project;
    template_name = 'climatefinance/index.html'
    context_object_name = 'project_list'


def project(request):
    return HttpResponse("This is a list of project")


def detail(request, item_id):
    project = Project.objects.get(pk=item_id)
    context = {
        'project':project,
    }
    return render(request, 'climatefinance/detail.html', context)

class ClimatefinanceDetail(DetailView):
    model = Project
    template_name = 'climatefinance/detail.html'


def create_project(request):
    form = ProjectForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('climatefinance:index')

    return render(request, 'climatefinance/project-form.html', {'form':form})

class CreateProject(CreateView):
    model = Project;
    fields = ['project_name', 'project_desc', 'project_price', 'project_image']
    template_name = 'climatefinance/project-form.html'

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



def about_us(request):
    return render(request, 'climatefinance/about.html')

def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('climatefinance:index')
    
    return render(request, 'climatefinance/project-form.html', {'form':form, 'project':project})

def delete_project(request, id):
    project = Project.objects.get(id=id)

    if request.method == 'POST':
        project.delete()
        return redirect('climatefinance:index')
    
    return render(request, 'climatefinance/project-delete.html', {'project': project})
