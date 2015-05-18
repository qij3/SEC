from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from sitegate.decorators import redirect_signedin, sitegate_view

from django.views.generic.list import ListView
import core.models as coremodels

class LandingView(TemplateView):
    template_name = 'base/index.html'

class TeamListView(ListView):
    model = coremodels.Team
    # template_name = 'team/list.html'
    template_name = 'base/theme.html'

@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})
