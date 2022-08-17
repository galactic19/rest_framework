from rest_framework import permissions


class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        '''
            인증된 유저에 한해 조회,등록을 허용 (permission 직접 구현해 보기)
            return: True/False
        '''
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user