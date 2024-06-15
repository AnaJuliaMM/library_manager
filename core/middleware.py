from django.utils.deprecation import MiddlewareMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class TokenAuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        token_auth = TokenAuthentication()
        auth = request.META.get('HTTP_AUTHORIZATION', '').split()
        if len(auth) == 2 and auth[0].lower() == 'token':
            try:
                user, token = token_auth.authenticate_credentials(auth[1])
                request.user = user
            except AuthenticationFailed:
                request.user = None
