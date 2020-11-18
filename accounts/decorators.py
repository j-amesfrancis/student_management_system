from django.shortcuts import redirect


def redirect_login(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper


def user_redirect(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.user_roles == 'staff':
            return redirect('staff-dashboard')
        elif request.user.user_roles == 'student':
            return redirect('student')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper
