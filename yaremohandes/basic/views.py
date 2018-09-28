from django.shortcuts import render
from django.views import generic
from basic.forms import NameForm
from basic.forms import MassageForm
# Create your views here.

# class index(generic.TemplateView):
#     template_name = 'main/index.html'

class About(generic.TemplateView):
    template_name = 'main/about.html'

class Software(generic.TemplateView):
    template_name = 'main/software.html'
#
# class Contact(generic.TemplateView):
#     template_name = 'main/contact.html'

class MyProfile(generic.TemplateView):
    template_name = 'main/myProfile.html'


def index(request):
    if request.method == 'POST':
        name_form = NameForm(data=request.POST)
        if name_form.is_valid():
            name = name_form.save()
        else:
            print (name_form.errors)

    else:
        name_form = NameForm()

    return render(request, 'main/index.html', {'name_form':name_form})

def Contact(request):
    if request.method == 'POST':
        massage_form = MassageForm(data=request.POST)
        if massage_form.is_valid():
            massage = massage_form.save()
        else:
            print (massage_form.errors)

    else:
        massage_form = MassageForm()

    return render(request, 'main/contact.html', {'massage_form':massage_form})

class Teaching(generic.TemplateView):
    template_name = 'main/teaching.html'
