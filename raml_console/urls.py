from django.conf.urls import url

from raml_console.views import console, renderer

urlpatterns = [
    url(r'^data/(?P<raml_file>.+)$', renderer, name='renderer'),
    url(r'^(?P<raml_file>.+)$', console, name='console'),
]
