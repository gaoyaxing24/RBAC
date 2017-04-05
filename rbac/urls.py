# coding: utf-8
"""rbac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from index import views as index_view, action as index_action
from staff import views as staff_view, action as staff_action

urlpatterns = [
    # --------------- 主页 -----------------
    url(r'^$', index_view.index),
    # 登录及登出
    url(r'^login$', index_view.login),
    url(r'^logout$', index_view.logout),
    url(r'^vlogin$', index_action.login),
    url(r'^vlogout$', index_action.logout),
    # ------------- 无权限 -----------------
    # 无权限页面
    url(r'^forbidden$', index_view.forbidden),
    # ------------ 测试 ----------------
    # 测试页面
    url(r'^test/page([1234]{1})$', staff_view.test_page),

    # ------------ RBAC 操作项 ------------
    # ------------ 用户 -------------------
    # 用户列表
    # 用户添加
    # 用户编辑

    # ------------ 角色 -------------------
    # 角色列表
    # 角色添加
    # 角色编辑

    # ------------ 权限 -------------------
    # 权限列表
    # 权限添加
    # 权限编辑
]
