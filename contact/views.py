from django.shortcuts import render, redirect
from .forms import ContactDetails
from .models import Contact
from .filters import Contactfilter

# Create your views here.
def index(request):
    contacts = Contact.objects.order_by('fullname')

    myFilter = Contactfilter(request.GET, queryset=contacts)
    contacts = myFilter.qs

    context = {'contacts': contacts, 'myFilter': myFilter}
    return render(request, 'index.html', context)


def profile(request, profile_id):
    contact = Contact.objects.get(pk=profile_id)

    context = {'contact': contact}
    return render(request, 'contact-profile.html', context)


def edit(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactDetails(instance=contact)

    if request.method == 'POST':
        form = ContactDetails(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return redirect('edit')
    context = {'form': form, 'contact': contact}
    return render(request, 'edit.html', context)


def addcontact(request):
    contact = ContactDetails()

    if request.method == 'POST':
        contact = ContactDetails(request.POST)
        if contact.is_valid():
            contact.save()
            print('success')
            return redirect('home')
        else:
            return redirect('create')
    context = {'contact': contact}
    return render(request, 'create-profile.html', context)

def deletecontact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)

    if request.method == 'POST':
        contact.delete()
        return redirect('home')

    context = {'contact': contact}
    return render(request, 'delete.html', context)