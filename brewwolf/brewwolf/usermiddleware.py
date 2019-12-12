from django.contrib.auth.middleware import RemoteUserMiddleware
from rest_framework.authentication import RemoteUserAuthentication


class IPForwardedMiddleware(RemoteUserMiddleware):
    header = "REMOTE_ADDR"


class IPForwardedAuthentication(RemoteUserAuthentication):
    header = "REMOTE_ADDR"
