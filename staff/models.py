# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class User(models.Model):
    """用户表"""
    # 用户名
    name = models.CharField(max_length=20, default='')
    # 邮件
    email = models.CharField(max_length=30, default='')
    # 是否管理员 0->非管理员     1->管理员
    is_admin = models.SmallIntegerField(default=0)
    # 状态 0->无效   1->有效
    status = models.SmallIntegerField(default=1)
    # 最后一次更新时间
    updated_time = models.DateTimeField(auto_now_add=True)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "用户->%s" % self.name


class Role(models.Model):
    """角色表"""
    # 角色名称
    name = models.CharField(max_length=20, default='')
    # 状态 0->无效   1->有效
    status = models.SmallIntegerField(default=1)
    # 最后一次更新时间
    updated_time = models.DateTimeField(auto_now_add=True)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "角色->%s" % self.name


class UserRole(models.Model):
    """用户 角色 关系表"""
    # 用户ID
    uid = models.IntegerField()
    # 角色ID
    role_id = models.IntegerField()
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)



class Access(models.Model):
    """权限表"""
    # 权限名称
    title = models.CharField(max_length=50, default='')
    # 权限名称对应的URLS   使用json存储
    urls = models.CharField(max_length=1000, default='')
    # 状态 0->无效, 1->有效
    status = models.SmallIntegerField(default=1)
    # 最后一次更新时间
    updated_time = models.DateTimeField(auto_now_add=True)
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "权限->%s" % self.title


class RoleAccess(models.Model):
    """角色权限关系表"""
    # 角色ID
    role_id = models.IntegerField()
    # 权限ID
    access_id = models.IntegerField()
    # 创建时间
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "角色权限->%s" % self.id

















