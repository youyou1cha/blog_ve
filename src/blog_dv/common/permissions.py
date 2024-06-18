from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwerOrReader(BasePermission):
    message = "发布者修改"

    @staticmethod
    def safe_methods_or_owner(request, func):
        if request.method in SAFE_METHODS:
            return func
        return func()

    def has_permission(self, request, view):
        '''
        登录验证
        :param request:
        :param view:
        :return:
        '''
        return self.safe_methods_or_owner(request, lambda: request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        '''
        修改权限
        :param request:
        :param view:
        :param obj:
        :return:
        '''

        return self.safe_methods_or_owner(request, lambda: obj.author == request.user)
