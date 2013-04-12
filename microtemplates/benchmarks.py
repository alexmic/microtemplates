import os
import timeit
from jinja2 import Environment, FileSystemLoader, Template as JinjaTemplate
from django.conf import settings
from django.template import Context, Template as DjangoTemplate
from django.template.loaders.filesystem import Loader as DjangoDefaultLoader
from django.template.loaders.cached import Loader as DjangoCachedLoader
from base import Template as MicroTemplate


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
context = {
    'title': 'MY TODOS',
    'todos': [
        dict(title='grocery shopping', description='do all the shopping', done=True, followers=[]),
        dict(title='pay bills', description='pay all the bills', done=False, followers=['alex']),
        dict(title='go clubbing', description='get drunk', done=False, followers=['alex', 'mike', 'paul']),
    ]
}

settings.configure(TEMPLATE_DIRS=[template_dir])

def read_html(engine):
    html_file_path = os.path.join(template_dir, "%s.html" % engine)
    with open(html_file_path) as html_file:
        html = html_file.read()
    return html


microtemplates_html = read_html('microtemplates')
django_html = read_html('django')
django_default_loader = DjangoDefaultLoader()
django_cached_loader = DjangoCachedLoader(['django.template.loaders.filesystem.Loader'])
jinja2_html = read_html('jinja2')
jinja2_env = Environment(loader=FileSystemLoader(template_dir))


def benchmark_microtemplates():
    MicroTemplate(microtemplates_html).render(**context)


def benchmark_django():
    DjangoTemplate(django_html).render(Context(context))


def benchmark_django_default_loader():
    template, _ = django_default_loader.load_template('django.html')
    template.render(Context(context))


def benchmark_django_cached_loader():
    template, _ = django_cached_loader.load_template('django.html')
    template.render(Context(context))


def benchmark_jinja2():
    JinjaTemplate(jinja2_html).render(**context)


def benchmark_jinja2_env():
    jinja2_env.get_template('jinja2.html').render(**context)


if __name__ == '__main__':
    number = 10000
    engines = ('microtemplates', 'django', 'django_default_loader', 'django_cached_loader', 'jinja2', 'jinja2_env')
    setup = "from __main__ import %s" % ', '.join(map(lambda t: 'benchmark_' + t, engines))
    for engine in engines:
        t = timeit.Timer("benchmark_%s()" % engine, setup=setup)
        time = t.timeit(number=number) / number
        print "%s => run %s times, took %.2f ms" % (engine, number, 1000 * time)
