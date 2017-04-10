# coding: utf-8
from __future__ import unicode_literals
from django.shortcuts import render

from staff.models import User


def index(request):
    """RBAC Index Page"""
    uid = request.COOKIES.get('uid')
    try:
        login_info = User.objects.get(id=uid)
    except Exception as e:
        login_info = None
    return render(request, "index.html", {"index_info": "主页", 'login_info': login_info})


def login(request):
    """登录"""
    return render(request, 'index.html', {"index_info": "测试登录页面"})


def logout(request):
    """登出"""
    return render(request, 'index.html', {"index_info": "测试登出页面"})


def forbidden(request):
    """拒绝访问, 没有权限"""
    return render(request, "forbidden.html")
