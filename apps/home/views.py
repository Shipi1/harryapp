from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1] #Esto lee la url, buscando por un archivo con ese nombre.

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist: #Si no hay template, tira 404.

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except: #nada, 500
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

'''
def botoncito(request):
    context = {}
    html_template = loader.get_template('home/botontest.html')
    return HttpResponse(html_template.render(context,request))
'''

'''def botoncito(request):
    # ...
    t = loader.get_template('home/botontest.html')
    #c = {
    #    'app': 'Harry app',
    #    'user': request.user,
    #    'ip_address': request.META['REMOTE_ADDR'],
    #    'message': 'Boton test'}
    context={}
    context['segment'] = "botontest"
    return t.render(context)'''

