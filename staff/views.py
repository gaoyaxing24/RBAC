# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render
from staff.models import User
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
