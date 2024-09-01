from django.shortcuts import render
from django.views.generic.base import View
from .models import Event, Ourteam, Sponsor, Participant, Winner

# Create your views here.

def home(request):
    return render(request, 'index.html')

def sabrang(request):
    return render(request, 'sabrang.html')

class sabrang22(View):
    def get(sel, request):
        event = Event.objects.filter(year="Sabrang 2022")
        context = {'event': event}
        return render(request, 'sabrang22.html', context)

class sabrang22view(View):
    def get(sel, request, myid):
        event = Event.objects.filter(year="Sabrang 2022")
        program = Event.objects.filter(id=myid)
        participant = Participant.objects.filter(event=myid)
        winner = Winner.objects.filter(event=myid)
        
        context = {'event': event, 'program':program[0], 'participant':participant, 'winner':winner}
        return render(request, 'sabrang22view.html', context)

class team(View):
    def get(sel, request):
        dignitaries = Ourteam.objects.filter(post="Dignitaries")
        commitee = Ourteam.objects.filter(post="Organizing Committee")
        core = Ourteam.objects.filter(post="Core Committee")
        print(dignitaries)

        context = {'core':core, 'commitee':commitee, 'dignitaries': dignitaries}
        return render(request, 'ourteam.html', context)

class sponsors(View):
    def get(sel, request):
        gold = Sponsor.objects.filter(sponsorstype="Gold Sponsor")
        event = Sponsor.objects.filter(sponsorstype="Event Sponsors")
        stall = Sponsor.objects.filter(sponsorstype="Stall Sponsors")
        stall2 = Sponsor.objects.filter(sponsorstype="Stall Sponsors")
        stall3 = Sponsor.objects.filter(sponsorstype="Stall Sponsors")
        printing = Sponsor.objects.filter(sponsorstype="Printing Partner")
        context = {'gold':gold, 'event':event, 'stall':stall[0:4], 'stall2':stall2[4:8], 'stall3':stall3[8:11], 'printing':printing}
        return render(request, 'sponsors.html',context)