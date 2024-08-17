from django.shortcuts import redirect


def is_login(view):

    def user_fun(req,*args, **kwargs):

        if req.user.is_authenticated:
            return redirect('workspace')

        return view(req,*args, **kwargs)

    return user_fun
