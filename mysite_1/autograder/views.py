from contextlib import redirect_stderr

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View

# Create your views here.


class mainview(LoginRequiredMixin, View):
    template_name = "autograder/main.html"
    success_url = reverse_lazy("autograder:main")

    def get(self, request):
        if request.user.is_authenticated:
            msg = request.session.get("msg", False)
            if msg:
                del request.session["msg"]
            return render(request, self.template_name, {"data": msg})

    def post(self, request):
        data = (
            (
                ((request.POST.get("field1")).strip()).casefold()
                + " "
                + ((request.POST.get("field2")).strip()).casefold()
            )
        )[::-1]
        request.session["msg"] = data
        return redirect(request.path)
