from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    # this is how we can overried below method and create custom authentication
    def authenticate(self, request):
        # here just randomly validating code for practice
        username = request.GET.get('username')
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            raise AuthenticationFailed('No such user')

        return super().authenticate(request)