from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.request import Request

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request: Request):
        username = request.META.get('HTTP_USERNAME')
        password = request.META.get('HTTP_PASSWORD')
        if not username or not password:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        user = authenticate(username=username, password=password)
        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password.'))

        return (user, None)