import os

from django.apps import apps
from django.utils._os import upath
from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse, Http404


def console(request, raml_file):
    return render(request, 'raml_console.html', {'raml_file': raml_file})


def renderer(request, raml_file):
    raml_file_args = raml_file.split('/')
    # assert len(raml_file_args) > 2, 'Invalid raml file path sepcified'
    # assert raml_file_args[-1].endswith('.raml'), 'Must specify a .raml file'

    for app_config in apps.get_app_configs():
        if not app_config.path:
            continue
        if app_config.name == raml_file_args[0]:
            # import pdb; pdb.set_trace()
            template_dir = os.path.join(
                app_config.path, 'raml', *raml_file_args[1:-1]
            )
            if os.path.isdir(template_dir):
                template_path = upath(template_dir)

                with open(
                    os.path.join(template_path, raml_file_args[-1]), 'r'
                ) as raml_file:
                    raml_contents = raml_file.read()

                template = Template(raml_contents)

                return HttpResponse(template.render(Context()))

    raise Http404
