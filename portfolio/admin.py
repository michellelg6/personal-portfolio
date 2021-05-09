from django.contrib import admin
from .models import Project
from .models import Skill
from .models import Service

# Register your models here.
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Service)