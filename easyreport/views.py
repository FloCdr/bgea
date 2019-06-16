from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms import modelformset_factory
from .models import *

def dashboard(request):

    return render(request, 'easyreport/dashboard.html')


def epreuve(request):

    if request.method == 'POST':

        form = EpreuveForm(request.POST)

        if form.is_valid():

            return HttpResponseRedirect('/alright/')

    else:
        form = modelformset_factory(Epreuve, extra=3, fields = '__all__')

    return render(request, 'easyreport/epreuve.html', {'formset' : form})


# Create your views here.
