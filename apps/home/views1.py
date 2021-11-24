#Views1 derived from .views, aquí pondremos funciones de front-end to back-end.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django import forms

class emocionesForm(forms.Form):
    #emocion = forms.
    descripcion = forms.CharField(label='descripcion', max_length=220)

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

def entrydiario(request): #Entrada de diario de emociones.

    t = loader.get_template('home/entrydiario.html')
    context = {}
    context['segment'] = "entrydiario"
    return HttpResponse(t.render(context))

'''def testForm(request):

    if request.method == 'POST':
        form = request.post

        arch = open("test.txt","w")
        arch.write(form)
        arch.close()
    return None'''

def testForm(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = emocionesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = emocionesForm()

    return render(request, 'botontest.html', {'form': form})