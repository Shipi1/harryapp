#Views1 derived from .views, aquí pondremos funciones de front-end to back-end.

from django.http import HttpResponse
from django.template import loader

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