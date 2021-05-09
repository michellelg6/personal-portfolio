from django.shortcuts import render
from .models import Project
from .models import Skill
from .models import Service

# Create your views here.
def home(request):

    projects = Project.objects.all()
    skills = Skill.objects.all()
    services = Service.objects.all()
    
    return render(request, 'portfolio/home.html', {'projects':projects, 'skills':skills, 'services':services })
    
   