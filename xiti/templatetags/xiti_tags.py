# -*- coding: utf-8 -*-
"""
Xiti tags
"""
from django.conf import settings
from django import template

from xiti.settings import XITI_CODE_TEMPLATE as DEFAULT_XITI_CODE_TEMPLATE

register = template.Library()

class XitiSettingsError(Exception):
    pass

@register.inclusion_tag(getattr(settings, 'XITI_CODE_TEMPLATE', DEFAULT_XITI_CODE_TEMPLATE), takes_context=True)
def xiti_code(context):
    """
    Tag code to load Xiti required HTML into your template

    Usage: ::

        {% load xiti_tags %}
        {% xiti_code %}
    """
    if not hasattr(settings, 'XITI_CONF'):
        raise XitiSettingsError("'XITI_CONF' is not defined in your settings")

    config = getattr(settings, 'XITI_CONF', {})

    if not config.get('xtsite', None) or not config.get('xiti_serverid', None):
        raise XitiSettingsError("'xtsite' and 'xiti_serverid' are required values in your 'settings.XITI_CONF'")

    # Pass request object to template tag context
    config = config.copy()
    config['request'] = context['request']
    return config
