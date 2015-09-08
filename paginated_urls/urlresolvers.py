# -*- coding: utf-8 -*-

"""

"""

from django.core.urlresolvers import reverse


def paginated_reverse(request, url_name, **kwargs):
    url = reverse(viewname=url_name, **kwargs)
    if request.user.is_authenticated():
        latest_paginated_url = request.session.get('latest_paginated_url')
        if latest_paginated_url['url_name'] == url_name:
            url = '{}?page={}'.format(url, latest_paginated_url['page'])
    return url
