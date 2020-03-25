from django.views.generic import TemplateView, RedirectView
from django.shortcuts import redirect, reverse


class LoginView(TemplateView):
    template_name = "management/presspass_login.html"

    def dispatch(self, request, *args, **kwargs):
        if self.request.session.get("presspass_authenticated", False) == True:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
