from django.contrib.auth.middleware import RemoteUserMiddleware


class RemoteAddrHeaderMiddleware(RemoteUserMiddleware):
    header = "USER_AGENT"
