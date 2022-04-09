from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View

# Create your views here.


class mainview(LoginRequiredMixin, View):
    template_name = "autograder/main.html"

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)

    def post(self, request):
        data = (
            (
                ((request.POST.get("field1")).strip()).casefold()
                + " "
                + ((request.POST.get("field2")).strip()).casefold()
            )
        )[::-1]
        ctx = {"data": data}
        return render(request, self.template_name, ctx)
