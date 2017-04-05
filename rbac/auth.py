# coding: utf-8
from __future__ import unicode_literals

from django.http import HttpResponseForbidden, HttpResponseRedirect
from staff.models import User, UserRole, Role, Access, RoleAccess


class AuthMiddleware(object):
    # 默认可以访问的地址
    __allow_url = {"before": [u'/', u'/login', u'/vlogin', '/forbidden'],
                   "after": [u'/logout', u'/vlogout', u'/', '/forbidden']
                  }

    def process_request(self, request):
        """决定调用哪个视图以前"""
        pass

    def process_view(self, request, view_func, view_args, view_kwargs):
        """如果访问的是以下控制器, 则必须事先登录"""
        if not self.__is_login(request):
            if not (request.path in self.__allow_url['before']):
                return HttpResponseRedirect('/forbidden')
        else:
            if not self.__is_super(request):
                has_perm = self.__has_perm(request)
                if not has_perm:
                    return HttpResponseRedirect('/forbidden')

    def __has_perm(self, request):
        """查看是否有此URL权限"""
        result = False
        if request.path in self.__allow_url['after']:
            result = True
        elif self.__is_super(request):
            result = True
        else:
            uid = request.COOKIES['uid']
            urls = request.path
            # 如果不是超级用户拿到 `用户所属的所有部门`
            user_role = UserRole.objects.filter(uid=uid)

            if user_role:
                role_id = [role.role_id for role in user_role]
            else:
                role_id = []

            # 获取 `部门所有的权限`
            perm_acc = RoleAccess.objects.filter(role_id__in=role_id)

            if perm_acc:
                access_id = [access.access_id for access in perm_acc]
            else:
                access_id = []

            # 确认此部门有此权限
            acc_info = Access.objects.filter(id__in=access_id, urls=urls)

            if acc_info:
                result = True

        return result





    def __is_super(self, request):
        """查看是否超级用户(管理员)"""
        result = False
        if 'iss' in request.COOKIES and request.COOKIES['iss'] == 1:
            result = True
        return False


    def __is_login(self, request):
        """查看是否登录"""
        is_login = False
        if 'uid' in request.COOKIES:
            is_login =  True
        return is_login
