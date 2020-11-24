from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import SignupForm
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import activation_token
from .email import send_activation_email
from django.utils.encoding import force_bytes


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    """
    View function for home page
    """
    return render(request, 'index/index.html')

def signup(request):
    User = get_user_model
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data.get('email')
            try:
                user = form.save(commit = False)
                user.is_active = False
                user.save()
                send_activation_email(request, user, email_address)
                return HttpResponse('Please confirm your email address to complete the registration')                
            except Exception as e:
                print("Exception: ", e)
    else:
        form = SignupForm()

    ctx = {'form':form}
    return render(request, 'django_registration/registration_form.html', ctx)

def activate(request, uid64, token):
    try:
        uid = force_text