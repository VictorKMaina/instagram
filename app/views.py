from django.shortcuts import render

# Create your views here.
def index(request):
    """
    View function for home page
    """
    return render(request, 'index/index.html')