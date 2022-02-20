from django.http import HttpResponse
from django.http.request import HttpRequest
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    """
    This is used to manage unauthenticated users

    Args:
        view_func (view): The passing view function
    """
    def wrapper_func(request, *args, **kwargs):
        """_summary_

        Args:
            request (HttpRequest): The http request from user

        Returns:
            View/ Direct('/'): If authentcated, it returns index html, otherwise error 404
        """
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    """
    User authorization for views of pages

    Args:
        allowed_roles (list, optional): Allowed user list. Defaults to [].
    """
    def decorator(view_func):
        """
        User authorization decorator

        Args:
            view_func (view): The view as funcion
        """
        def wrapper_func(request, *args, **kwargs):
            """
            The decorator wrap function

            Args:
                request (httprequest): Http request from an user

            Returns:
                Wrapper_func: decorator wrapped function
            """
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('not authenticated')

        return wrapper_func
    return decorator