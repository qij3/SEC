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

from django.template import RequestContext
from django.shortcuts import render_to_response

#Regsiter
# from core.forms import UserForm, UserProfileForm
from core.forms import UserForm
from django.db import transaction

#Login
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

# Logout and redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Logout message alert
from django.contrib import messages

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
    fields =['members', 'name', 'email', 'company', 'skills', 'industry', 'description', 'image_file']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(ProfileCreateView, self).form_valid(form)

    def get_success_url(self):
        return '/profile/'


class ProfileUpdateView(UpdateView):
    model = coremodels.Profile
    template_name = 'base/form.html'
    fields =['members', 'name', 'email', 'company', 'skills', 'industry', 'description', 'image_file']

'''
@sitegate_view(widget_attrs={'class': 'form-control', 'placeholder': lambda f: f.label}, template='form_bootstrap3') # This also prevents logged in users from accessing our sign in/sign up page.
def entrance(request):

    return render(request, 'base/entrance.html', {'title': 'Sign in & Sign up'})
'''
@transaction.atomic
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            login(request, new_user)
            return HttpResponseRedirect('/profile/create')
        # Invalid form or forms - mistakes or something else?
        else:
            messages.success(request, user_form.errors)
            return HttpResponseRedirect('/signup/')

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'base/signup.html',
            {'user_form': user_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                messages.success(request, 'Login Successfully.')
                return HttpResponseRedirect('/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            messages.success(request, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

            return HttpResponseRedirect("/login/")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('base/login.html', {}, context)

def logout_view(request, next_page=None,
           template_name='team/list.html',
           redirect_field_name='team',
           current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    logout(request)
    messages.success(request, 'Log Out Successfully.')

    # Redirect goes index page
    return HttpResponseRedirect('/')
