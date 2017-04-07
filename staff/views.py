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


def access_list(request):
    """权限列表"""
    accesses = Access.objects.all()
    return render(request, "staff/accessList.html", {'accesses': accesses})


def access_add(request):
    """权限添加 页面"""
    return render(request, "staff/accessAdd.html")


def access_edit(request):
    """权限编辑 页面"""
    aid = request.GET.get('aid')
    try:
        access = Access.objects.get(id=aid)
    except Exception:
        access = None
    return render(request, "staff/accessEdit.html", {"access": access})

