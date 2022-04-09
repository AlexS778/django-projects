from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View

# Create your views here.


class mainview(LoginRequiredMixin, View):
    template_name = "autograder/main.html"
    success_url = reverse_lazy("ads:all")

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)

    def post(self, request):
        data = (
            (
                (request.POST.get("Field1")).strip()
                + " "
                + (request.POST.get("Field2")).strip()
            )
        )[::-1]
        data.casefold()
        return HttpResponse(data)
