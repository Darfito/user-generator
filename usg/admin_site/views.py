from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    return render(request, 'base.html')
<<<<<<< HEAD

def user(request):
    return render(request, 'user.html')
=======
def projectView(request):
    return render(request, 'project-view.html')
>>>>>>> admin-project-view
