from ads.models import Ad
from ads.owner import (
    OwnerCreateView,
    OwnerDeleteView,
    OwnerDetailView,
    OwnerListView,
    OwnerUpdateView,
)


class AdsListView(OwnerListView):
    model = Ad


class AdsDetailView(OwnerDetailView):
    model = Ad


class AdsCreateView(OwnerCreateView):
    model = Ad
    fields = ["title", "text"]


class AdsUpdateView(OwnerUpdateView):
    model = Ad
    fields = ["title", "text"]


class AdsDeleteView(OwnerDeleteView):
    model = Ad