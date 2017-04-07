# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from staff.models import User, Role, Access
from django.http import HttpResponse


def test_page(request, page):
    """RBAC Test Pages"""
    page_dict = dict(zip("1234", "一二三四"))
    return render(request, "test/page.html", {"pages": page_dict[str(page)]})


def user_list(request):
    """用户列表 页面"""
    users = User.objects.all()
    return render(request, 'staff/staffList.html', {"users": users})


def user_add(request):
    """用户添加 页面"""
    return render(request, 'staff/staffAdd.html', {})


def user_edit(request):
    """用户编辑 页面"""
    uid = request.GET['uid']
    user = User.objects.get(id=uid)
    return render(request, 'staff/staffEdit.html', {'user': user})


def role_list(request):
    """角色列表 页面"""
    roles = Role.objects.all()
    return render(request, "staff/roleList.html", {"roles": roles})


def role_add(request):
    """角色添加 页面"""
    return render(request, 'staff/roleAdd.html')


def role_edit(request):
    """角色编辑 页面"""
    rid = request.GET.get('rid')
    try:
        role = Role.objects.get(id=rid)
    except Exception:
        role = None

    return render(request, "staff/roleEdit.html", {"role": role})



