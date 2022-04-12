from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Search(View):
    def get(self, request):
        strval = request.GET.get("search")
        print(strval)

        # if strval:
        #     # Simple title-only search
        #     # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

        #     # Multi-field search
        #     # __icontains for case-insensitive search
        #     query = Q(title__contains=strval)
        #     query.add(Q(text__contains=strval), Q.OR)
        #     ad_list = (
        #         Ad.objects.filter(query).select_related().order_by("-updated_at")[:10]
        #     )
        # else:
        #     ad_list = Ad.objects.all().order_by("-updated_at")[:10]
        return render(request, "unesco/search.html")

    # def post(self, request):
    #     self.data = request.POST.get("field1")
    #     return render(request, "unesco/search.html")
