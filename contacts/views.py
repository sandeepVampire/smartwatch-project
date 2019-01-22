from django.shortcuts import render
from contacts.models import Contacts
from django.http import HttpResponseRedirect
# Create your views here.
def view(request):
    contacts = Contacts.objects.all()
    return render(request, 'contact.html',{'contacts':contacts})
def addview(request):
    return render(request,'add.html',{})

def newview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        contact = Contacts()
        contact.first_name = name
        contact.phone = phone
        contact.save()
    return HttpResponseRedirect('http://localhost:8000/contact/')


