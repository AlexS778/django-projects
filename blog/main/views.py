from django.shortcuts import render

from .models import Post


def mainpage(request):
    po = Post.objects.all()
    ctx = {"post": po}
    return render(request, "main/main.html", ctx)
