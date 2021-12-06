#Views1 derived from .views, aquí pondremos funciones de front-end to back-end.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from . import forms, models

def botoncito(request): #"Chuleta" (como dice la Sofi) de llamar una función.

    t = loader.get_template('home/botontest.html')
    #c = {
    #    'app': 'Harry app',
    #    'user': request.user,
    #    'ip_address': request.META['REMOTE_ADDR'],
    #    'message': 'Boton test'}
    context={}
    context['segment'] = "botontest"
    return HttpResponse(t.render(context))

def samplepage(request):
    t=loader.get_template('home/page-blank.html')
    c = {}
    c['segment'] = 'sample'
    return HttpResponse(t.render(c))

#def entrydiario(request): #Entrada de diario de emociones. <- No borrar, tal vez se use como referencia.

#    t = loader.get_template('home/entrydiario.html')
#   context = {}
#    context['segment'] = "entrydiario"
#   return HttpResponse(t.render(context))

def entrydiario(request): #Entrada de diario de emociones,

    if request.method == "POST":
        formulario = forms.EmocionesForm(request.POST)
        if formulario.is_valid(): #De aquí se guarda e interpreta la información de las emociones.

            print(formulario.cleaned_data['emocion'])
            print(formulario.cleaned_data['descripcion'])

            entrada = models.entradaDiario(emocion=formulario.cleaned_data['emocion'],descripcion=formulario.cleaned_data['descripcion'])
            entrada.save()

            return render(request, "home/diario.html")
    else:
        formulario = forms.EmocionesForm()

    return render(request, "home/entrydiario.html", {"form":formulario})

def diario(request):
    entradas = models.entradaDiario.objects.all()
    return render(request, 'home/diario.html', {'entradas':entradas})


def testForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.emocionesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/botoncito/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.emocionesForm()

    return render(request, 'botontest.html', {'form': form})