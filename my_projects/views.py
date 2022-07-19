from multiprocessing import context
from urllib import request
from django.shortcuts import render
from my_projects.models import Projects


def project_index(request):
    projects = Projects.objects.all()
    context = {'projects': projects}
    return render(request, 'my_projects/project_index.html', context)


def project_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'my_projects/project_detail.html', context)
    

