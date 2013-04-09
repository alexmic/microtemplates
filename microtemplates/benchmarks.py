import os
import timeit
from jinja2 import Template as JinjaTemplate
from django.conf import settings
from django.template import Context, Template as DjangoTemplate
from .base import Template as MicroTemplate

settings.configure()

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
context = {
    'title': 'MY TODOS',
    'todos': [
        dict(title='grocery shopping', description='do all the shopping', done=True, followers=[]),
        dict(title='pay bills', description='pay all the bills', done=False, followers=['alex']),
        dict(title='go clubbing', description='get drunk', done=False, followers=['alex', 'mike', 'paul']),
    ]
}


def read_html(engine):
    html_file_path = os.path.join(template_dir, "%s.html" % engine)
    with open(html_file_path) as html_file:
        html = html_file.read()
    return html


def benchmark_microtemplates():
    html = read_html('microtemplates')
    MicroTemplate(html).render(**context)


def benchmark_django():
    html = read_html('django')
    DjangoTemplate(html).render(Context(context))


def benchmark_jinja2():
    html = read_html('jinja2')
    JinjaTemplate(html).render(**context)


if __name__ == '__main__':
    number = 1000
    engines = ('microtemplates', 'django', 'jinja2')
    setup = "from __main__ import %s" % ', '.join(map(lambda t: 'benchmark_' + t, engines))
    for engine in engines:
        t = timeit.Timer("benchmark_%s()" % engine, setup=setup)
        time = t.timeit(number=number) / number
        print "%s => run %s times, took %.2f ms" % (engine, number, 1000 * time)

