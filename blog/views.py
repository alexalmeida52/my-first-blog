from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here. 12345

def post_list(request):
    return render(request, 'blog/post_list.html', {})