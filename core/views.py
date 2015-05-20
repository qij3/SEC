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
from django.views.generic.edit import CreateView, UpdateView

# Logout and redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


class LandingView(TemplateView):
    template_name = 'base/index.html'


# Team Views
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


class TeamUpdateView(UpdateView):
    model = coremodels.Team
    template_name = 'base/form.html'
    fields = "__all__"


# Profile Views
class ProfileListView(ListView):
    model = coremodels.Profile
    template_name = 'profile/list.html'
    paginate_by = 5


class ProfileDetailView(DetailView):
    model = coremodels.Profile
    template_name = 'profile/detail.html'
    context_object_name = 'profile'


class ProfileCreateView(CreateView):
    model = coremodels.Profile
    template_name = 'base/form.html'
    fields = ['members', 'working_status', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(ProfileCreateView, self).form_valid(form)

    def get_success_url(self):
        return self.object.members.get_absolute_url()


class ProfileUpdateView(UpdateView):
    model = coremodels.Profile
    template_name = 'base/form.html'
    fields = ['members', 'working_status', 'description']


@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):
    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})

def logout_view(request, next_page=None,
           template_name='team/list.html',
           redirect_field_name='team',
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    logout(request)
    # Redirect goes index page
    return HttpResponseRedirect('/')
