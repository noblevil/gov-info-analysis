#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__ = 'noblevil'
__date__ = '2017/2/25 15:07'

from urlparse import urljoin
from urlparse import urlparse
from urlparse import urlunparse
from posixpath import normpath


def myjoin(base, url):
    url1 = urljoin(base, url)
    arr = urlparse(url1)
    path = normpath(arr[2])
    return urlunparse((arr.scheme, arr.netloc, path, arr.params, arr.query, arr.fragment))