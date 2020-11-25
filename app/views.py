from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .email import send_activation_email
from .forms import SignupForm
from .models import *
from .token import activation_token

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    """
    View function for home page
    """
    images = Image.objects.order_by('id').reverse()
    ctx = {'images':images}
    return render(request, 'index/index.html', ctx)


def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data.get('email')
            user = form.save(commit = False)
            user.is_active = False
            user.save()
            send_activation_email(request, user, email_address)
            return HttpResponseRedirect('/accounts/confirm-email/')               
    else:
        form = SignupForm()

    ctx = {'form':form}
    return render(request, 'django_registration/registration_form.html', ctx)

def confirm_email(request):
    return render(request, 'django_registration/registration_complete.html')

def activate(request, uid, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except:
        user = None
    ctx = {'uid':uid, 'token':token}
    if user is not None and activation_token.check_token(user, token):
        profile = Profile(user = user, bio = "I'm a leo.")
        user.is_active = True
        user.profile = profile
        user.save()
        profile.save_profile()
        login(request, user)

        return HttpResponseRedirect('/', ctx)

        login(request, user)
    else:
        return render(request, 'django_registration/activation_failed.html', ctx)
