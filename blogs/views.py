from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category
from .models import Blogs
from jobs.models import Jobs
# Create your views here.
def index(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    jobs = Jobs.objects.all()
    return render(request,"frontend/index.html",{'Categories':categories,'blogs': blogs,'jobs': jobs})
    