from django.shortcuts import render
from datetime import datetime
from .forms import searchForm, uploadForm
from django.http import HttpResponseRedirect
from django.conf import settings
import os
theme = settings.THEME
import debug
debug.DEBUG = os.getenv('DEBUG')
DATA = False
from .models import config as cfg
import vping  #vping(dest_addr, timeout=2, count=4)
from soundpark import soundpark
from pprint import pprint

#def ping(dest_addr):
    #return vping.vping(dest_addr)

def config():
    data_config = {
        'theme': settings.THEME,
        'static_url': cfg.objects.filter(pk = 1).get().static_url,
        'media_url': cfg.objects.filter(pk = 1).get().media_url,
        'base': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'base.html'),
        'header': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'header.html'),
        'custom_css': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'custom_css.html'),
        'style_css': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'style_css.html'),
    }
    return data_config

def sound_park():
    proxies = ['https://192.168.1.1:3128', 'http://192.168.1.1:3128']
    c = soundpark.soundpark(proxies = proxies, debug = False)
    #days_top = c.days_top()
    return (c.days_top())

def handle_upload_file(f):
    with open('file.jpg', 'wb') as destination:
        for chuck in f.chuck:
            destination.write(chuck)
            
def handle_search(POST):
    global DATA
    DATA = POST.get('query')

def search(request):
    if request.method == 'POST':
        form = searchForm(request.POST)
        if form.is_valid():
            debug.debug(request_POST = request.POST)
            debug.debug(type_request_POST = type(request.POST))
            handle_search(request.POST)
            return HttpResponseRedirect('/home')

def home(request):
    debug.debug(user_agent = request.META.get('HTTP_USER_AGENT'))
    global theme
    theme = 'default'
    html_file = os.path.join(theme, 'index.html')
    form = searchForm()
    search(request)
    context = config()
    isAlive = vping.vping('google.com')
    if isAlive:
        context.update({'isAlive': True,})
    else:
        context.update({'isAlive': False,})
    if vping.vping('8.8.8.8'):
        soundpark_days_top = sound_park()
        pprint(soundpark_days_top)
    else:
        soundpark_days_top = {}
    #debug.debug(soundpark_days_top = soundpark_days_top)
    context.update({        
        'form': form,
        'action': '/home/',
        'base': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'base.html'),
        'title': 'Fast download mp3 for free',
        'copyright' : '&copy %s LICFACE' % (datetime.now().year),
        'data': DATA,
        'user_agent': request.META.get('HTTP_USER_AGENT'),
    })
    debug.debug(context_META = context)
    return render(request, html_file, context= context)

def tag(request):
    debug.debug(user_agent = request.META.get('HTTP_USER_AGENT'))
    global theme
    theme = 'default'
    html_file = os.path.join(theme, 'tag.html')
    form = searchForm()
    search(request)
    context = config()
    isAlive = vping.vping('google.com')
    if isAlive:
        context.update({'isAlive': True,})
    else:
        context.update({'isAlive': False,})
    if vping.vping('8.8.8.8'):
        soundpark_days_top = sound_park()
        pprint(soundpark_days_top)
    else:
        soundpark_days_top = {}
    #debug.debug(soundpark_days_top = soundpark_days_top)
    context.update({        
        'form': form,
        'action': '/home/',
        'base': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'base.html'),
        'title': 'Fast download mp3 for free',
        'copyright' : '&copy %s LICFACE' % (datetime.now().year),
        'data': DATA,
        'user_agent': request.META.get('HTTP_USER_AGENT'),
        'custom_css': os.path.join(theme, 'tag_custom_css.html'), 
        'style': os.path.join(theme, 'tag_style_css.html'), 
    })
    debug.debug(context_META = context)
    return render(request, html_file, context= context)

def upload(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILE['files'])
            return HttpResponseRedirect('/home')
    else:
        form = uploadForm()

    html_file = os.path.join(theme, 'home.html')
    context = config()
    context.update({
        'action': '/home/upload/',
        'form': form,
        'base': os.path.join(settings.TEMPLATES[0].get('DIRS')[0], theme, 'base', 'base.html'),
    })
    return render(request, html_file, context= context)