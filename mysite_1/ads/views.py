from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View

from ads.forms import CommentForm, CreateForm
from ads.models import Ad, Comment
from ads.owner import (
    OwnerCreateView,
    OwnerDeleteView,
    OwnerDetailView,
    OwnerListView,
    OwnerUpdateView,
)


class ForumsListView(OwnerListView):
    model = Ad
    template_name = "ads/list.html"


class ForumDetailView(OwnerDetailView):
    model = Ad
    template_name = "ads/detail.html"

    def get(self, request, pk):
        x = Ad.objects.get(id=pk)
        comments = Comment.objects.filter(ad=x).order_by("-updated_at")
        comment_form = CommentForm()
        context = {"ad": x, "comments": comments, "comment_form": comment_form}
        return render(request, self.template_name, context)


class ForumsCreateView(LoginRequiredMixin, View):
    template_name = "ads/form.html"
    success_url = reverse_lazy("ads:all")

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {"form": form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class ForumsUpdateView(LoginRequiredMixin, View):
    template_name = "ads/form.html"
    success_url = reverse_lazy("pics:all")

    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {"form": form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {"form": form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class ForumsDeleteView(OwnerDeleteView):
    model = Ad
    template_name = "ads/delete.html"


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST["comment"], owner=request.user, ad=f)
        comment.save()
        return redirect(reverse("ads:ad_detail", args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "ads/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse("ads:ad_detail", args=[ad.id])


def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response["Content-Type"] = ad.content_type
    response["Content-Length"] = len(ad.picture)
    response.write(ad.picture)
    return response
