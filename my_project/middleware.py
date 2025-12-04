# middleware.py
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
import re

EXEMPT_URLS = [
    re.compile(r'^/admin/'),               # allow admin and its pages
    re.compile(r'^/static/'),              # static files
    re.compile(r'^/media/'),               # media files
    re.compile(r'^/accounts/login/?$'),    # login page
    re.compile(r'^/accounts/logout/?$'),   # logout
    re.compile(r'^/accounts/password_reset'),  # optional
    re.compile(r'^/favicon.ico$'),
]

class LoginRequiredMiddleware:
    """
    Redirect anonymous users to LOGIN_URL except for EXEMPT_URLS.
    Put after AuthenticationMiddleware in settings.MIDDLEWARE.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # You can extend EXEMPT_URLS from settings if needed
        custom = getattr(settings, "LOGIN_EXEMPT_URLS", [])
        for pattern in custom:
            EXEMPT_URLS.append(re.compile(pattern))

    def __call__(self, request):
        # If user is authenticated, continue
        if request.user.is_authenticated:
            return self.get_response(request)

        path = request.path_info  # /some/path/
        # Allow matching exempt urls
        for pattern in EXEMPT_URLS:
            if pattern.match(path):
                return self.get_response(request)

        # Not exempt and not authenticated -> redirect to login
        login_url = settings.LOGIN_URL
        # optional: keep next param so user returns after login
        return redirect(f"{login_url}?next={request.path}")
