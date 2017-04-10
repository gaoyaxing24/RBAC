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


def set_role(request):
    """设置角色 操作
    1.取出表单中的uid及表单中提交上来的设置角色列表
    2. 获取到所有的角色
    3. 如果根本此uid和rid获取到了此角色且在roles列表中, 则保留, 否则删除
    4. 如果未根本uid和rid取到到此角色此在roles列表中, 则新建, 否则pass
    """
    uid = request.POST['uid']
    roles = request.POST.getlist('roles')
    all_rid = [str(role.id) for role in Role.objects.all()]
    for rid in all_rid:
        try:
           user_role = UserRole.objects.get(uid=uid, role_id=rid)
        except Exception:
            if rid in roles:
                user_role = UserRole()
                user_role.uid = uid
                user_role.role_id = rid
                user_role.save()
        else:
            if rid not in roles:
                user_role.delete()
    return HttpResponseRedirect(reverse('staff_list'))


def set_access(request):
    """设置权限 操作"""
    rid = request.POST['rid']
    accesses = request.POST.getlist('accesses')
    all_aid = [str(access.id) for access in Access.objects.all()]
    for aid in all_aid:
        try:
            role_access = RoleAccess.objects.get(role_id=rid, access_id=aid)
        except Exception:
            if aid in accesses:
                role_access = RoleAccess()
                role_access.role_id = rid
                role_access.access_id = aid
                role_access.save()
        else:
            if aid not in accesses:
                role_access.delete()
    return HttpResponseRedirect(reverse('role_list'))
