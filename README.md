microtemplates.py
=================

A toy templating engine. Accompanying blog post:
[http://alexmic.net/building-a-template-engine/](http://alexmic.net/building-a-template-engine/).

## Why?

I just wanted to learn how to write a templating engine. It's not feature-complete or production-ready.
It's a playground and it will be a work in progress.

## Documentation

There are two types of tags, `blocks` and `variables`.

### Variables

```html
<div>{{my_var}}</div>
```

### Blocks

There are three types of blocks – `if`, `each` and `call`.

#### Loops

```html
{% each items %}
    <div>{{it}}</div>
{% end %}

{% each [1,2,3] %}
    <div>{{it}}</div>
{% end %}
```

`it` references the current item in the iteration and it is scoped to this item's
attributes. To access attributes of the parent context use `..`. For example:

```html
{% each items %}
    <div>{{..name}}</div><div>{{it}}</div>
{% end %}
```

#### Conditionals

Supported operators are: `>, >=, <, <=, ==, !=`. You can also use conditionals
with things that evaluate to truth.

```html
{% if num > 5 %}
    <div>more</div>
{% else %}
    <div>less or equal</div>
{% end %}

{% if items %}
    <div>we have items</div>
{% end %}
```

#### Callables

Callables can get passed positional or keyword arguments.

```html
<div class='date'>{% call prettify date_created %}</div>
<div>{% call log 'here' verbosity='debug' %}</div>
```

## Benchmarks

Using `benchmarks.py` and the templates files in `templates/` here are the results:

```
microtemplates => run 10000 times, took 0.36 ms
django => run 10000 times, took 0.95 ms
django_default_loader => run 10000 times, took 1.16 ms
django_cached_loader => run 10000 times, took 0.46 ms
jinja2 => run 10000 times, took 5.64 ms
jinja2_env => run 10000 times, took 0.08 ms
```