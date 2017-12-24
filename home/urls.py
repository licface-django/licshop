from django.conf.urls import url
from django.conf import settings
#from django.conf.urls.static import static
from django.contrib.staticfiles import views as vserve
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.home), 
    url(r'^upload/', views.upload), 
    url(r'^search/', views.home), 
    url(r'^images/(?P<path>.*)$', vserve.serve),
]

urlpatterns += staticfiles_urlpatterns()