from django.http.response import HttpResponsePermanentRedirect


def login_required(function_to_decorate):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function_to_decorate(request, *args, **kwargs)
        else:
            return HttpResponsePermanentRedirect("/login/")

    return wrapper


def test_decorate(function_to_decorate):
    def wrapper(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return function_to_decorate(self, request, *args, **kwargs)
        else:
            return HttpResponsePermanentRedirect("/login/")

    return wrapper
