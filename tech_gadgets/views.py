from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from .dummy_data import gadgets, manufacturer
import json
from django.utils.text import slugify
from django.views import View
from django.views.generic.base import RedirectView

def start_page_view(request):
    return HttpResponse('hey, das hat doch gut funktioniert')

# wandelt die id/nummer in einen Slug um und redirectet zu slug url
#ist gadgets_id kleiner als die tatsächliche länge von gadgets (Dummy-daten) wird redirectet ansonsten gibt es einenen fehler 404
def gadgets_int_view(request, gadgets_id):
    if(len(gadgets)) > gadgets_id:
        new_slug = slugify(gadgets[gadgets_id]['name'])
        new_url = reverse('gadgets_slug_url', args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound('Sy, Gadget was not found!')

# Slugify den namen von Dummy-Data und vergleichen es mit der Url, die ja schon slugify ist
# Http404() zeigt die originale und eigentliche 404 seite an, die man berbeiten und sehen kann.
def slug_gadgets_view(request, gadgets_slug):
    gadgets_match = None
    for gadget in gadgets:
        if slugify(gadget['name']) == gadgets_slug:
            gadgets_match = {'result' : gadget}
    if gadgets_match:   
        return JsonResponse(gadgets_match)
    raise Http404()

# zum Posten von Daten
#   Fehlerquelle  JsonResponse({'response':':) Erfolgreich daten hochgeladen!'})
# ist der Response ein Json? {}? KeyValuePair? ...
def gadget_post_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8")) 
            print(f'received data:{data}')
            return JsonResponse({'response':':) Erfolgreich daten hochgeladen!'})
        except:
            return JsonResponse({'response': ':( Daten konnten nicht hochgeladen werden!'})

# Post und Get Funktion in einer -> da diese aber zu groß und zu unübersichtlich ist, ist es angebracht die Klassen von Dangoi zu nehmen, 
# die schon vordifinierte Funktionen bereitstellt.
'''
def single_gadgets_view_utils(request, gadgets_slug = ''):
    if request.method == 'GET':
        gadgets_match = None
        for gadget in gadgets:
            if slugify(gadget['name']) == gadgets_slug:
                gadgets_match = {'result' : gadget}
        if gadgets_match:   
            return JsonResponse(gadgets_match)
        raise Http404()
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode("utf-8")) 
            print(f'received data:{data}')
            return JsonResponse({'response':':) Erfolgreich daten hochgeladen!'})
        except:
            return JsonResponse({'response': ':( Daten konnten nicht hochgeladen werden!'})
    return HttpResponse('No Method Found!')
 '''

# !! pattern_name ist wichtig -> dieser ist in der urls diffiniert -> path('<slug:gadgets_slug>', GadgetsView.as_view(), name='gadgets_slug_url')
#    gadget_id = kwargs.get('gadgets_id',0) ist wichtig, um aus den kwargs die argumente zu ziehen, die man brauch. die zweite stelle, `,0` gibt einen default-wert an, wenn wert leer.
class RedirectGadgets(RedirectView):
    pattern_name = 'gadgets_slug_url'
    def get_redirect_url(self, *args, **kwargs):
        gadget_id = kwargs.get('gadgets_id',0)
        new_kwargs = {'gadgets_slug': '4k-ultrahd-monitor'}
        if(len(gadgets)) > gadget_id:
            new_slug = slugify(gadgets[gadget_id]['name'])
            new_kwargs = {'gadgets_slug': new_slug}
        return super().get_redirect_url(*args, **new_kwargs)

# https://docs.djangoproject.com/en/5.0/topics/class-based-views/intro/
class GadgetsView(View):

    def get(self, request, gadgets_slug):
        gadgets_match = None
        for gadget in gadgets:
            if slugify(gadget['name']) == gadgets_slug:
                gadgets_match = {'result' : gadget}
        if gadgets_match:   
            return JsonResponse(gadgets_match)
        raise Http404()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8")) 
            print(f'received data:{data}')
            return JsonResponse({'response':':) Erfolgreich daten hochgeladen!'})
        except:
            return JsonResponse({'response': ':( Daten konnten nicht hochgeladen werden!'})
        return HttpResponse('No Method Found!')
    
# Mehr für Template arbeiten und dessen Sprache in Django -> https://docs.djangoproject.com/en/5.0/ref/templates/language/#templates
# {'gadget_list': gadgets} übergibt an das Template/HTML gadget_list für die for Schleife.
def tech_gadgets_tes_render_view(request):

    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})


class ManafatcoryRedirect(RedirectView):
      pattern_name = 'factory_slug_url'
      def get_redirect_url(self, *args, **kwargs):
        id_of_factory = kwargs.get('factory_id')
        new_kwargs = {'factory_slug': 'hometech-co'}
        if(len(manufacturer) > id_of_factory):
            new_slug = slugify(manufacturer[id_of_factory]['name'])
            new_kwargs = {'factory_slug': new_slug}
        return super().get_redirect_url(*args, **new_kwargs)


class Manafatcory(View):
    def get(self, request, factory_slug):
        factory_match = None
        for factory in manufacturer:
            if slugify(factory['name']) == factory_slug:
                factory_match = {'result' : factory}
        if factory_match:
            return JsonResponse(factory_match)
        raise Http404()

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body.decode("utf-8")) 
            print(f'received data:{data}')
            return JsonResponse({'response': f':) Erfolgreich daten hochgeladen! {data}' })
        except:
            return JsonResponse({'response': ':( Daten konnten nicht hochgeladen werden!'})
        