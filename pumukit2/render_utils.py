# -*- coding: utf-8 -*-
#

import logging
import pkg_resources

from django.template import Context, Template

log = logging.getLogger(__name__)

def load_resource(resource_path):
    """
    Gets the content of a resource
    """
    resource_content = pkg_resources.resource_string(__name__, resource_path)

    return unicode(resource_content)


def render_template(template_path, context={}):
    """
    Evaluate a template by resource path, applying the provided context
    """
    template_str = load_resource(template_path)
    template = Template(template_str)

    return template.render(Context(context))