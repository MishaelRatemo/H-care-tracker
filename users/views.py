from django.shortcuts import render
from django.core.mail import send_mail
from django.template import Context
from django.views.generic import FormView, UpdateView
from django.urls import reverse, reverse_lazy
from users.forms import LoginForm, SignupForm
from tracker.models import Profile
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    form = SignupForm
    title= ' Welcome'
    context ={ 'title': title, 'form': form}
    return render(request, 'signup.html', context)

@login_required(login_url='login')
def login(request):
    form = LoginForm
    title = "Welcome"
    context = {'form':form, 'title':title}
    return render(request, 'login.html', context)


class SignupView(FormView):
    """Signup View."""
    template_name = 'users/templates/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """If the form is valid save the user"""
        form.save()
        return super().form_valid(form)

# class LoginView(auth_views.LoginView):
#     """Login view"""
#     template_name = 'users/login.html'
#     redirect_authenticated_user = True

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view"""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['name', 'email', 'contact', 'facility']
    # Return success url
    def get_object(self):
        """Return user's profile"""
        return self.request.user.profile
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username_slug': username})
