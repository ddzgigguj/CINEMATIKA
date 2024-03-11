from django.shortcuts import render
from . import models

def about(request):
    post_objects = models.People.objects.all()
    context = {
        'post_ke': post_objects,
    }
    template_name = 'films/about.html'
    return render(request, template_name, context)
