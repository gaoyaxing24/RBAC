# coding: utf-8
#!/usr/bin/env python
"""
    created by: Gao YaXing
    created on: 17/4/4
"""

from __future__ import unicode_literals

import json
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from staff.models import User, Role, UserRole, Access, RoleAccess


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
        res = HttpResponse
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


def user_add(request):
    """用户添加 操作"""
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()

    user = User.objects.create(name=name, email=email)

    try:
        user.save()
    except Exception as e:
        print('保存出错了, %s', e)
    return HttpResponseRedirect(reverse('staff_list'))


def user_edit(request):
    """用户编辑 操作"""
    uid = request.POST.get('uid', '').strip()
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()

    try:
        user = User.objects.get(id=uid)
    except Exception as e:
        user = None

    if user:
        user.name = name
        user.email = email
        user.save()

    return HttpResponseRedirect(reverse('staff_list'))


def role_add(request):
    """角色添加 操作"""
    name = request.POST.get('name', '').strip()
    role = Role.objects.create(name=name, status=1)
    try:
        role.save()
    except Exception:
        pass
    return HttpResponseRedirect(reverse("role_list"))


def role_edit(request):
    """角色编辑 操作"""
    rid = request.POST.get('rid')
    name = request.POST.get('name')
    try:
        role = Role.objects.get(id=rid)
    except Exception:
        role = None

    if role:
        role.name = name
        role.save()
    return HttpResponseRedirect(reverse('role_list'))


def access_add(request):
    """权限添加 操作"""
    title = request.POST.get('title', '').strip()
    urls = request.POST.get('urls', '').strip()

    access = Access.objects.create(title=title, urls=urls, status=1)
    try:
        access.save()
    except Exception:
        pass
    return HttpResponseRedirect(reverse('access_list'))


def access_edit(request):
    """权限编辑 操作"""
    aid = request.POST.get('aid')
    title = request.POST.get('title', '').strip()
    urls = request.POST.get('urls', '').strip()

    try:
        access = Access.objects.get(id=aid)
    except Exception:
        access = None

    if access:
        access.title = title
        access.urls = urls
        access.save()

    return HttpResponseRedirect(reverse('access_list'))

