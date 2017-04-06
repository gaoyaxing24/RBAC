# coding: utf-8
#!/usr/bin/env python
"""
    created by: Gao YaXing
    created on: 17/4/4
"""

import json
from django.http import HttpResponse, HttpResponseRedirect

from staff.models import User, UserRole, Access, RoleAccess


def login(request):
    """登录"""
    uid = request.GET.get('uid')
    if not uid:
        return HttpResponseRedirect(u'/', {"index_info", '登录必须有UID'})

    try:
        user = User.objects.get(id=uid)
    except Exception as e:
        user = None

    if user:
        res = HttpResponseRedirect("/")
        res.set_cookie('uid', uid)
        if user.is_admin:
            res.set_cookie('iss', 1)
        return res
    return HttpResponseRedirect('/')


def logout(request):
    """登出"""
    response = HttpResponseRedirect("/login")
    if 'uid' in request.COOKIES:
        response.delete_cookie('uid')
    if 'iss' in request.COOKIES:
        response.delete_cookie('iss')
    return response
