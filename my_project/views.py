# views.py
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def home_redirect(request):
    """
    Redirect '/' depending on authentication:
    - logged-in -> /files/
    - anonymous -> /accounts/login/
    """
    if request.user.is_authenticated:
        return redirect('/files/')
    return redirect('/accounts/login/')


class CustomLoginView(LoginView):
    template_name = "login.html"

    def form_valid(self, form):
        # If "remember" is unchecked -> session expires on browser close
        remember = self.request.POST.get('remember')
        if not remember:
            self.request.session.set_expiry(0)  # expires on browser close
        else:
            self.request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
        return super().form_valid(form)


