from django.shortcuts import render
from .models import Projet
from .forms import message_form
from django.core.mail import send_mail
from django.conf import settings
def Index(request):
    return render(request, 'main/home.html')

# Create your views here.
def Home(request):
    Projets = Projet.objects.all()
    context = {'Projets': Projets,}
    return render(request, 'main/index.html', context)

def Contact(request):
    context = {}
    if request.method == "POST":
        form = message_form(request.POST)
        if form.is_valid():
            form.save()
            prénom = form.cleaned_data.get('prénom')
            nom = form.cleaned_data.get('nom')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')
            to = 'contact@kujenga-architectes.com'

            subject = 'Nouveau message sur votre application !'
            message = 'de :' + email + '| message : ' + message
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [to]

            send_mail(subject, message, email_from, recipient_list)

            context['prénom'] = prénom
            return render(request, 'main/message_reçu.html', context)
        else:
            form = message_form()
            context['form'] = form
            return render(request, 'main/contact.html', context)
    else:
        form = message_form(request.POST)
        context['form'] = form
        return render(request, 'main/contact.html', context)

    return render(request, 'main/contact.html')

def Team(request):
    return render(request, 'main/Team.html')

def Portfolio(request):
    projets = Projet.objects.all()
    context = {'projets':projets}
    return render(request, 'main/Portfolio.html', context)

def Project(request, pk):
    projet= Projet.objects.get(pk=pk)
    context = {}
    context['Projet'] = projet
    return render(request, 'main/projet.html', context)

def A_propos(request):
    return render(request, 'main/a_propos.html')

def Profile_Dania(request):
    return render(request, 'main/profile_Dania.html')

def Profile_Inou(request):
    return render(request, 'main/profile_Inou.html')

def Profile_Mambadi(request):
    return render(request, 'main/profile_Mambadi.html')

def Profile_Houza(request):
    return render(request, 'main/profile_Houza.html')
