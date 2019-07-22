from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
# Create your views here.

from bootstrap.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name' , 'email', 'address']

def contact_list(request, template_name='bootstrap/contact_list.html'):
    contact = Contact.objects.all()
    return render(request, template_name, {'id': 0, 'contact_list': contact})

def contact_create(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('bootstrap:bootstrap_list')

def contact_update(request, pk):
    contact= get_object_or_404(Contact, pk=(pk-1))
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
    return redirect('bootstrap:bootstrap_list')


def contact_delete(request, pk):
    contact= get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('bootstrap:bootstrap_list')


def contact_select(request, pk, template_name='bootstrap/contact_list.html'):
    contact = Contact.objects.get(pk=pk)
    arrVal = Contact.objects.all()
    return render(request, 
                  template_name, 
                  {'name': contact.name, 
                   'email': contact.email, 
                   'address':contact.address, 
                   'id': contact.id+1, 
                   'contact_list': arrVal})
