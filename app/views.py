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
    comments = Comment.objects.order_by('id').reverse()
    current_user = request.user
    profile = Profile.find_by_user(current_user)

    ctx = {'images':images, 'Comment':Comment, "profile":profile}
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

@login_required(login_url='/accounts/login/')
def add_like(request):
    try:
        image_id = request.POST.get('image_id')
        image = Image.find_by_id(image_id)
        image.add_like()

        return HttpResponse("success")
    except:
        return HttpResponse("failed")

@login_required(login_url='/accounts/login/')
def add_comment(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        comment_post = request.POST.get('comment')
        if image_id is not None and comment_post is not None:
            current_user = request.user
            profile = Profile.find_by_user(current_user)
            image = Image.find_by_id(image_id)
            comment = Comment(profile = profile, image = image, comment = comment_post)
            comment.save_comment()

            print("COMMENT: ", comment)

            return HttpResponse("success")
    else:
        return HttpResponse("failed")

@login_required(login_url='/accounts/login/')
def image(request, image_id):
    current_user = request.user
    profile = Profile.find_by_user(current_user)
    image = Image.find_by_id(image_id)
    comments = Comment.find_by_image(image)
    ctx = {"image":image, "comments":comments, "current_profile":profile}
    return render(request, 'index/single_image.html', ctx)

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    profile = Profile.find_by_user(current_user)
    ctx = {"profile":profile}
    return render(request, 'index/new_image.html', ctx)