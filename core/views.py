from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from sitegate.decorators import redirect_signedin, sitegate_view

# Creating list view
from django.views.generic.list import ListView
import core.models as coremodels

# Creating Details view
from django.views.generic.detail import DetailView

# Create Create view
from django.views.generic.edit import CreateView

class LandingView(TemplateView):
    template_name = 'base/index.html'

class TeamListView(ListView):
    model = coremodels.Team
    template_name = 'team/list.html'
    paginate_by = 5

class TeamDetailView(DetailView):
    model = coremodels.Team
    template_name = 'team/detail.html'
    context_object_name = 'team'

class TeamCreateView(CreateView):
  model = coremodels.Team
  template_name = 'base/form.html'
  fields = "__all__"


@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

