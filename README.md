microtemplates.py
=================

A toy templating engine. Accompanying blog post:
[http://alexmic.net/building-a-template-engine/](http://alexmic.net/building-a-template-engine/).

## Why?

I just wanted to learn how to write a templating engine. It's not feature-complete or production-ready.
It's a playground and it will be a work in progress.

## Documentation

There are *two* types of tags, *blocks* and *variables*.

### Variables

```html
<div>{{my_var}}</div>
```

### Blocks

There are *three* types of blocks – `if`, `each` and `call`.

#### Loops

```html
{% each items %}
    <div>{{it}}</div>
{% endeach %}

{% each [1,2,3] %}
    <div>{{it}}</div>
{% endeach %}
```

`it` references the current item in the iteration and it is scoped to this item's
attributes. To access attributes of the parent context use `..`. For example:

```html
{% each items %}
    <div>{{..name}}</div><div>{{it}}</div>
{% endeach %}
```

#### Conditionals


#### Callables