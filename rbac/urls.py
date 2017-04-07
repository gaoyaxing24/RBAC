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
    url(r'^$', index_view.index, name='index'),
    # 登录及登出
    url(r'^login$', index_view.login, name='login'),
    url(r'^logout$', index_view.logout, name='logout'),
    url(r'^vlogin$', index_action.login, name='vlogin'),
    url(r'^vlogout$', index_action.logout, name='vlogout'),
    # ------------- 无权限 -----------------
    # 无权限页面
    url(r'^forbidden$', index_view.forbidden),
    # ------------ 测试 ----------------
    # 测试页面
    url(r'^test/page/([1234]{1})$', staff_view.test_page, name='test_page'),

    # ------------ RBAC 操作项 ------------
    # ------------ 用户 -------------------
    # 用户列表
    url(r'^staff/list$', staff_view.user_list, name='staff_list'),
    # 用户添加  页面
    url(r'^staff/add$', staff_view.user_add, name='staff_add'),
    # 用户添加  操作
    url(r'^staff/add/action$', staff_action.user_add, name='staff_add_act'),
    # 用户编辑  页面
    url(r'^staff/edit$', staff_view.user_edit, name='staff_edit'),
    # 用户编辑  操作
    url(r'^staff/edit/action$', staff_action.user_edit, name='staff_edit_act'),
    # 设置用户角色 页面

    # 设置用户角色 操作

    # ------------ 角色 -------------------
    # 角色列表 页面
    url(r'^role/list$', staff_view.role_list, name='role_list'),
    # 角色添加 页面
    url(r'^role/add$', staff_view.role_add, name='role_add'),
    # 角色添加 操作
    url(r'^role/add/action$', staff_action.role_add, name='role_add_act'),
    # 角色编辑 页面
    url(r'^role/edit$', staff_view.role_edit, name='role_edit'),
    # 角色编辑 编辑
    url(r'^role/edit/action$', staff_action.role_edit, name='role_edit_act'),

    # 设置角色权限 页面

    # 设置角色权限 操作


    # ------------ 权限 -------------------
    # 权限列表
    url(r'^access/list$', staff_view.access_list, name='access_list'),
    # 权限添加 页面
    url(r'^access/add$', staff_view.access_add, name='access_add'),
    # 权限添加 编辑
    url(r'^access/add/action$', staff_action.access_add, name='access_add_act'),
    # 权限编辑 页面
    url(r'^access/edit$', staff_view.access_edit, name='access_edit'),
    # 权限编辑 编辑
    url(r'^access/edit/action$', staff_action.access_edit, name='access_edit_act'),
]
