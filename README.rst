.. _Django: https://www.djangoproject.com/

===========
Django Xiti
===========

Django app to include Xiti loading code into your templates

This is a very basic app that does not contains any view, just a template tag to build the HTML code to load Xiti in your site pages.

It relies on Xiti parameters defined in your settings.

Links
*****

* Download his `PyPi package <https://pypi.python.org/pypi/django-xiti>`_;
* Clone it on his `repository <https://github.com/emencia/django-xiti>`_;

Requires
********

* `Django`_ >= 1.4;

Install
*******

First install the package ::

    pip install django-xiti

Add it to your installed Django apps in settings : ::

    INSTALLED_APPS = (
        ...
        'xiti',
        ...
    )

Then fill your Xiti paramters in your settings: ::

    XITI_CONF = {
        'xiti_serverid': '', # Xiti server ID for usage on http protocole
        'xiti_serverid_secure': '', # Xiti server ID for usage on https protocole
        'xtsite': '', # Xiti site ID, also named 's'
        'xtn2': '', # level 2 site ID, also named 's2'
        'xtpage': '', # page name (with the use of :: to create chapters), also named 'p'
        'xtdi': '', # implication degree, also named 'di'
        'xt_an': '', # user ID, also named 'an'
        'xt_ac': '', # category ID, also named 'ac'
        'xt_multc': '', # all the xi indicators (like "&x1=...&x2=....&x3=...")
    }

All these parameters are generated for your site from your Xiti account. ``xiti_serverid`` and ``xtsite`` values are required. If required values are not filled, ``xiti_code`` usage will raise a exception ``XitiSettingsError``.

Loading 'xtcore.js'
-------------------

Finally, **you must have the Xiti Javascript core file** ``xtcore.js`` **in your static**. This file is not shipped into this app because it can be different from a site to another, you need to download it from your Xiti account.

When you got it, just put it as ``js/xtcore.js`` into your staticfiles directory. If you want to use another path or to load it differently you can override template ``xiti/include_js.html`` in your templates directory.

Generally, you should not try to load it without this template, because Xiti Javascript core must be loaded after parameters are defined else it won't be able to use them, resulting in blank report.

Usage
*****

Just use the template tag into your templates: ::

    {% load xiti_tags %}
    {% xiti_code %}

This tag does not accept any argument.