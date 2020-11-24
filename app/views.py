from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    """
    View function for home page
    """
    return render(request, 'index/index.html')