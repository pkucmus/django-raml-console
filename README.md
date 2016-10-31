# Django RAML console

##Quick start

1. Add "raml_console" to your INSTALLED_APPS setting like this:

```
INSTALLED_APPS = [
    ...
    'raml_console',
]
```

2. Include the raml_console URLconf in your project urls.py like this:

```
url(r'^raml/', include('raml_console.urls')),
```

3. Visit http://127.0.0.1:8000/raml/<app_name>/<raml_file> to access the console.
